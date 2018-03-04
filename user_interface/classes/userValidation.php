<?php

class loadProperties {
    
    private $index;
    private $capcha;
    private $error;
    
    function __construct() {
        //$this->index = stream_get_contents(fopen('index.txt', 'r'));
        $this->error = json_decode(file_get_contents('../errors/errors.json'), TRUE);
        $this->capcha = json_decode(file_get_contents('../json/capcha.json'), TRUE);
        $this->index = rand(1, (count($this->getError()) - 1));
    }

    function getIndex() {
        return $this->index;
    }

    function getCapcha() {
        return $this->capcha;
    }

    function getError() {
        return $this->error;
    }

        
    function verifCapcha($field, $model) {

        $result = TRUE;
        if ( ($field == 'oui') && ($model == FALSE) || ($field == 'non') && ($model == TRUE)){
            $result = FALSE;
        } 
        return $result;
    }

    function addLog($data, $comment) {
        // On ouvre en lecture/écriture pour créer le fichier si il n'existe pas
                fopen('../json/resolveLog.json', "w+");
                    // Tableau contenan les informations que l'on vas encoder
                    $initJson = array(
                    $data => $comment,
                    );
                file_put_contents('../json/resolveLog.json', json_encode($initJson));  // On encode et on écris le tableau dans le fichier JSON
    }
    private function setIndex($index) {
        //$this->index = $index;
    }

        
    function updateIndex() {
//        $this->setIndex(intval($this->getIndex())+ 1);
//        $buffer = $this->getIndex();
//        $buffer = strval($buffer);
//        $fichier = fopen('index.txt', 'w');
//        fwrite($fichier, $buffer); 
    }

}

function afficheForm() {
    
    $proc = new loadProperties();
    
    $index = intval($proc->getIndex());
    $jsonTab = $proc->getError();
    $capcha = $proc->getCapcha();
    $model = true;
    if ($index % 2 === 0) {
        $model = false;
    }
    $finalData = $jsonTab[$index];
    $data2 = $capcha[$index];
    if ( isset($_POST['envoyer']) ) {
        
        //$proc->updateIndex();
        $secure = new Data_Validation();
        
        //DonnéeValidée
        $oui = ( $_POST['prop2'] == 'true') ? TRUE : FALSE;
        if ( ! $oui && $secure->verifText($secure->cancelSpecialChara($_POST['comment']))) {
            $proc->addLog($finalData ,$_POST['comment']);
        }

    }
    
    echo '<div>';
    $form = new Form_Manager('', 'form', 'POST', 'visitorValidation');
    
    $form->proposition($finalData);
    
    $form->TDBF_Display_radio(array(true => 'oui', false => 'non'), '', 'prop2', 'radio');
    $form->TDBF_Display_text('Entrez votre commentaire', 'comment', 'textZone', '');
    
    $form->retourChariot(2);
    //   
    //    $form->proposition($finalData);
    //    $form->TDBF_Display_radio(['oui','non'], '', 'prop1', 'radio');
    //    $form->TDBF_Display_text('Entrez votre commentaire', 'fauxComment', 'textZone', '');
    //    
    //    $form->retourChariot(2);
    
    $form->TDBF_Display_button('envoyer', 'envoyer', 'envoyer', 'submit');
    $form->display();
    echo '</div>';
}
afficheForm();