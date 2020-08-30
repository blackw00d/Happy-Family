<?php

/**
 * Telegram Bot Api class
 *
 * @api
 * @since PHP 5.4
 * @author Pavel Kuznetsov [pk@webportnoy.ru]
 * @link https://core.telegram.org/bots/api
 *
*/

class TelegramBotApi{

	const VERSION = '1.1';

	protected $apiToken = null;

	protected $apiUrl = "https://api.telegram.org/bot";

	protected $chatId = null;

	public $debug = true;

	public $proxy = "";

    public function __construct( $token = null ){
		if( isset( $token ) ){
			$this->apiToken = $token;
		}
		else{
            throw new Exception('Required "token" not supplied in construct');
		}
	}


    public function send_to_channel($text)
    {
        return $this->request('/sendMessage?chat_id=-1001258399827&text='.urlencode($text).'&parse_mode=HTML');
    }

    private function request($p_function, $img=null)
    {
        $l_uri = $this->apiUrl . $this->apiToken. $p_function;
        $l_curl = curl_init($l_uri);
        if ($img){
            curl_setopt($l_curl, CURLOPT_HTTPHEADER, array("Content-Type:multipart/form-data"));
            curl_setopt($l_curl, CURLOPT_POSTFIELDS, array('photo' => new CURLFile(realpath($img))));
        }
        curl_setopt($l_curl, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($l_curl, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($l_curl, CURLOPT_SSL_VERIFYHOST, false);
        $l_curlResult = curl_exec($l_curl);
        if ($l_curlResult === false) return false;;
        $dec = json_decode($l_curlResult, true);
        curl_close($l_curl);
        if (!$dec) {
            return false;
        } else {
            return $dec;
        }
    }
}

?>