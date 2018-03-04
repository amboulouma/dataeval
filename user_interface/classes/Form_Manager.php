<?php

/**
 * Description of Form_Manager
 * 
 * @author joHNkHaN_scr
 */
class Form_Manager {
    
    private $action;
    private $class;
    private $method;
    private $formulaire_element = array();
    
    public function __construct( $action, $class = "", $method = "POST", $id = NULL) {
        $this->action = $action;
        $this->class = $class;
        $this->method= $method;
        $this->id= $id;
    }
    
    public function retourChariot($nbSaut) {
        
        for ($index = 0; $index < $nbSaut; $index++) {
            $r = '<br>';
        }
        array_push($this->formulaire_element, $r);
        
    }

    public function proposition($data) {
        
        $r = 'Cette donnée est peut-être érronée, quand pensez-vous? <br>'.$data.'<br>';
        array_push ( $this->formulaire_element, $r );
    }
    
    public function display() {
        echo '<form method="' . $this->method . '" action="' . $this->action . '" class="' . $this->class . '" id="' . $this->id . '">';
        foreach ($this->formulaire_element as $element){
            echo $element;
        }
        echo '</form>';
    }
    /**
     * 
     * @param array $tabOptions taleaux contenans les chaine à placer entre les balise option
     * @param string $label l\"étiquette
     * @param string $name pour le nom et l\"ID
     * @param string $class pour la class css
     * @return string un champ de selection
     */
    public function TDBF_Display_select ( $tabOptions, $label, $name, $class ='', $errorMsg = false, $default = null ) {
        
        if ( !is_array($tabOptions) or !is_string($label) or !is_string($name) or !is_string($class) ){
            trigger_error("param entry is not valid!");
        }
        else {       
           
            $r = "<div class='box_" . $name . "'>";
            
            // On affiche le message d'erreur s'il y en a
            if( $errorMsg ) $r .= "<p class=\"error-input\">" . $errorMsg . "</p>";
            
            $r .= "<label for=\"" . $name . "\">" . $label . "</label>
                <select id=\"" . $name . "\" name=\"" . $name . 
                "\" class=\"" . $class . "\">
            ";
            foreach( $tabOptions as $key => $option ) {
                if( strval($key) === $default ) {
                    $selected = "selected='selected'";
                }
                else {
                    $selected = '';
                }
                
                $r .="\t<option " . $selected . " value=\"" . $key . "\">" . $option . "</option>\n\t";
            }
            $r .= "    </select></div>";

            array_push ( $this->formulaire_element, $r );
        }
    }

    /**
     * 
     * @param string $name pour le nom et l\"ID
     * @param string $class pour la class css
     * @param string $value pour le titre du bouton
     * @return string un bouton
     */
    public function TDBF_Display_button ( $name, $class, $value,  $type = 'button') {
        if ( !is_string($name) or !is_string($class) 
                and !(is_string($value) or is_int($value) ) ){
            trigger_error("param entry is not valid!");
        }
        else {  
            $r = "
                <div class='box_" . $name . "' id='box_" . $name . "'>
                    <input type=\"" . $type . "\" id=\"" . $name . "\" name=\"" . $name .  
                "\" class=\"" . $class . "\" value=\"" . $value . "\" />
                </div>
            ";

            array_push ( $this->formulaire_element, $r );
        }
    }

    /**
     * 
     * @param string $label l\"étiquette
     * @param string $name pour le nom et l\"ID
     * @param string $class pour la class css
     * @return string un champ de selection de date
     */
    public function TDBF_Display_date ( $label, $name, $class, $errorMsg = false ) {
        if ( !is_string($label) or !is_string($name) or !is_string($class) ){
            trigger_error("param entry is not valid!");
        }
        else {  
            $r = "<div class='box_" . $name . "'>";
            
            // On affiche le message d'erreur s'il y en a
            if( $errorMsg ) $r .= "<p class=\"error-input\">" . $errorMsg . "</p>";
            
            $r .= "<label for=\"" . $name . "\">" . $label . "</label>
                <input type=\"date\" id=\"" . $name . "\" name=\"" . $name . 
                "\" class=\"" . $class ."\"/>
                </div>
            ";

            array_push ( $this->formulaire_element, $r );
        }
    }

    /**
     * 
     * @param string $label l\"étiquette
     * @param string $name pour le nom et l\"ID
     * @param string $class pour la class css
     * @param string $value le texte temporaire
     * @return string un champ de saisie
     */
    public function TDBF_Display_text ( $label, $name, $class, $value = '', $errorMsg = false ) {
        if ( !is_string($label) or !is_string($name) or !is_string($class)
                and !(is_string($value) or is_int($value) ) ){
            trigger_error("param entry is not valid!");
        }
        else {  
            $r = "<div class='box_" . $name . "'  id = 'box_" . $name . "'>";
            
            // On affiche le message d'erreur s'il y en a
            if( $errorMsg ) $r .= "<p class=\"error-input\">" . $errorMsg . "</p>";
            
                
            $r .= "<label for=\"" . $name . "\">" . $label . "</label>
                <input type=\"text\" id=\"" . $name . "\" name=\"" . $name .  
                "\" class=\"" . $class . "\" value=\"" . $value ."\"/>
                </div>
            ";

            array_push ( $this->formulaire_element, $r );
        }
    }

    /**
     * 
     * @param string $label l\"étiquette
     * @param string $name pour le nom et l\"ID
     * @param string $class pour la class css
     * @param type $value le texte temporaire
     * @return string un champ de saisie de password
     */
    public function TDBF_Display_password ( $label, $name, $class, $value = '', $errorMsg = false ) {
        if ( !is_string($label) or !is_string($name) or !is_string($class) ){
            trigger_error("param entry is not valid!");
        }
        else {  
            $r = "<div class='box_" . $name . "'>";
            
            // On affiche le message d'erreur s'il y en a
            if( $errorMsg ) $r .= "<p class=\"error-input\">" . $errorMsg . "</p>";
            
            $r .= "<label for=\"" . $name . "\">" . $label . "</label>
                <input type=\"password\" id=\"" . $name . "\" name=\"" . $name .  
                "\" class=\"" . $class . "\" value=\"" . $value . "\"/>
                </div>
            ";

            array_push ( $this->formulaire_element, $r );
        }
    }

    public function TDBF_Display_radio( $tabOptions, $label, $name, $class ) {
        if ( !is_string($label) or !is_string($name) or !is_string($class) ){
            trigger_error("param entry is not valid!");
        }
        else {  
            $r = "<div class='box_" . $name . "'>";
            
            $r .= "<label for=\"" . $name . "\">" . $label . "</label>";
            
            $compteur = 0;
            foreach($tabOptions as $value => $libelle) {
                $isChecked = ( $compteur == 0 ) ? 'checked' : '';
                $r .= "<input type='radio' id='" . $name . "' name='" . $name . "' value='" . $value . "' $isChecked>" . $libelle;
                $compteur++;
            }
            
            $r .= "</div>
            ";

            array_push ( $this->formulaire_element, $r );
        }
    }
    
    /**
     * 
     * @param string $name pour le nom et l\"ID
     * @param string $link pour le lien href
     * @param string $class pour la class css
     * @param string $value pour le titre du bouton
     * @return string un bouton
     */
    public function TDBF_Display_button_link ( $name, $link, $class, $value, $type = 'button' ) {
        if ( !is_string($name) or !is_string($class) 
                and !(is_string($value) or is_int($value) ) ){
            trigger_error("param entry is not valid!");
        }
        else {  
            $r = "
                <div class='box_" . $name . "'>
                    <a href=\"" . $link . "\"><input type=\"" . $type . "\" id=\"" . $name . "\" name=\"" . $name .  
                "\" class=\"" . $class . "\" value=\"" . $value . "\" /></a>
                </div>
            ";

            array_push ( $this->formulaire_element, $r );
        }
    }
    
    /**
     * 
     * @param string $label
     * @param string$name
     * @param string$id_html
     * @param string$class
     * @param string $value
     * @param string $errorMsg
     */
    public function TDBF_Display_date_input( $label, $name, $id_html = '', $class = '', $value = '', $errorMsg = false ) {
        if ( !is_string($label) or !is_string($name) or !is_string($class) ){
            trigger_error("param entry is not valid!");
        }
        else {  
            if( $value != '' ) {
                $tab_value = explode('/', $value);
                $value_jour = 'value="' . $tab_value[0] . '"';
                $value_mois = 'value="' . $tab_value[1] . '"';
                $value_annee = 'value="' . $tab_value[2] . '"';
            }
            else {
                $value_jour = '';
                $value_mois = '';
                $value_annee = '';
            }
            
            $r = "<div class='box_" . $class. "' id= '" . $id_html . "'>";
            
            // On affiche le message d'erreur s'il y en a
            if( $errorMsg ) $r .= "<p class=\"error-input\">" . $errorMsg . "</p>";
            $r .= "<span>" . $label . "</span>";
            
            $r.= "<span class='" . $class . "'>";
            // jour
            $r .= "<label for=\"" . $name . "-jour\">Jour</label>";
            $r .= "<input type=\"number\" class='jour' id=\"" . $name . "-jour\" " . $value_jour . " name=\"" . $name . "-jour\" min='1' max='31'>";

            // mois
            $r .= "<label for=\"" . $name . "-mois\">Mois</label>";
            $r .= "<input type=\"number\" class='mois' id=\"" . $name . "-mois\" " . $value_mois . " name=\"" . $name . "-mois\"/ min='1' max='12'>";
            
            // années
            $r .= "<label for=\"" . $name . "-annees\">Années</label>";
            $r .= "<input type=\"number\" class='annee' id=\"" . $name . "-annee\" " . $value_annee . " name=\"" . $name . "-annees\" min='1111' max='9999'>";

            $r.= "</span>";
            $r .= "</div>";
            array_push ( $this->formulaire_element, $r );
        }
    }

}