
<?php

class Data_Validation {

 
    /**
    * Verifie que la donnes soit une chaine de caractères sans nombre
    *
    * @param string $donnes
    * 
    * @return $donnes verifié
    */
    public function verifText($donnes){
        $val_return = false;
        if(is_string($donnes)){
            $pattern = '#^[A-Za-zéè\'çàê ë-]+$#';
            if(preg_match($pattern, $donnes)){
                $val_return = true;
            }
        }
        return $val_return;
    }

    
    /**
    * Definie une limite de caractères à la donnes passé en parametre
    *
    * @param string $donnes
    * @param int $numberMin
    * @param int $numberMax
    * 
    * @return $donnes verifié
    */
    public function limitChara($donnes, $numberMin, $numberMax){
        $val_return = false;
        if(is_string($donnes)){
            if(strlen($donnes) <= $numberMax AND strlen($donnes) >= $numberMin){
                $val_return = true;
            }
        }
        return $val_return;
    }
    /**
    * Verifie la présence et annules les charactère speciaux present dans la chaine
    *
    * @param string $donnes
    * 
    * @return $donnes verifié
    */
    public function cancelSpecialChara($donnes){
        // verifie que la donnes ne comprend pas de chara perso
          $donnes = htmlspecialchars($donnes);
        return $donnes;
    }
}