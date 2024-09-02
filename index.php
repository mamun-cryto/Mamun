<?php
session_start();
ob_start();
include "lib.php";
include "config.php";
//tokenni yozing
$admin = "7411781986";
//ozizni id raqamizni yozing
function bot($method, $datas = [])
{
	$url = "https://api.telegram.org/bot" . API_KEY . "/" . $method;
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_POSTFIELDS, $datas);
	$res = curl_exec($ch);
	if (curl_error($ch)) {
		var_dump(curl_error($ch));
	} else {
		return json_decode($res);
	}
}

$replyc = json_encode([
	'resize_keyboard' => false,
	'force_reply' => true,
	'selective' => true
]);

$update = json_decode(file_get_contents('php://input'));
$efede = json_decode(file_get_contents('php://input'), true);
$message = $update->message;

//files
$text = $message->text;
$usertext = $update->message->text;
$photo = $update->message->photo;
$gif = $update->message->animation;
$video = $update->message->video;
$music = $update->message->audio;
$voice = $update->message->voice;
$sticker = $update->message->sticker;
$document = $update->message->document;

//group
$ctitle = $update->message->chat->title;
$cuname = $update->message->chat->username;
$chat_id = $update->message->chat->id;
$cid = $update->message->chat->id;
$turi = $update->message->chat->type;

$data = $update->callback_query->data;
$qid = $update->callback_query->id;
$callcid = $update->callback_query->message->chat->id;
$clid = $update->callback_query->from->id;
$callmid = $update->callback_query->message->message_id;
$gid = $update->callback_query->message->chat->id;

//user
$ufname = $update->message->from->first_name;
$uname = $update->message->from->last_name;
$ulogin = $update->message->from->username;
$user_id = $update->message->from->id;

//reply

$id = $message->reply_to_message->from->id;
$repmid = $message->reply_to_message->message_id;
$repname = $message->reply_to_message->from->first_name;
$repulogin = $message->reply_to_message->from->username;
$reply = $message->reply_to_message;
$sreply = $message->reply_to_message->text;
$mes_id = $update->message->message_id;

$mes_idd = $message->message_id;
$from_id = $message->from->id;
$mid = $message->message_id;
$amid = $message->admin->message_id;
$forid = $update->message->forward_from->message_id;
$edname = $editm->from->first_name;
$forward = $update->message->forward_from;
$editm = $update->edited_message;
$fadmin = $message->from->id;
//bu yerni o'zgartirishingiz mumkin.
$fadmin = $message->from->id;
$from = $message->from;

$new_chat_members = $message->new_chat_member->id;
$new_fname = $message->new_chat_member->first_name;
$username = $message->from->username;
$fname = $message->from->first_name;
$lname = $message->from->last_name;
$is_bot = $message->new_chat_member->is_bot;
function inlinekeyboard($i, $t, $k)
{
	bot('sendMessage', [
		'chat_id' => $i,
		'text' => "$t",
		'parse_mode' => "HTML",
		'reply_to_message_id' => $mes_id,
		'reply_markup' => json_encode([
			'inline_keyboard' => $k,
			"resize_keyboard" => true,
			'one_time_keyboard' => false,
		])
	]);
}

$come = file_get_contents("https://api.telegram.org/bot" . API_KEY . "/getMe");
$deco = json_decode($come, true);
$botid = $deco["result"]["id"];
$botusername = $deco["result"]["username"];
if ($text == "/start" or substr($text, 0, 6) == "/start") {
  $ids = explode(" ",$text);
  $id = $ids[1];
  $checkfile="Admin/already/$from_id.txt";
  $balancefile="Admin/balance/$from_id.txt";

action($from_id, "typing");
  if($id !=""){
  if(file_exists($checkfile)){
    Message($from_id,"<b>⛔️ You Have already Started the Bot</b>");
  }else{
    file_put_contents("Admin/already/$from_id.txt","");
    file_put_contents($balancefile,"0")
;  
    $old=file_get_contents ("Admin/total/users.txt");
    file_put_contents ("Admin/total/users.txt",$old+1);
    if($from_id ==$id){Message($from_id,"❌️ You Cannot Invite Yourself");}else{
       $refuser=file_get_contents("Admin/balance/$id.txt");
    file_put_contents ("Admin/balance/$id.txt",$refuser+$per_refer);
          Message($from_id,"<b>🚀 You Wre Refered By $id</b>");
    Message($id,"<b>New Referrral $from_id +$per_refer Rs</b>");
    }
  }
}else{
  if(file_exists($checkfile)){
    Message($from_id,"<b>⛔️ You Have already Started the Bot</b>");
    
  }else{
   file_put_contents("Admin/already/$from_id.txt","");
    file_put_contents ($balancefile,"0");
        $old=file_get_contents ("Admin/total/users.txt");
    file_put_contents ("Admin/total/users.txt",$old+1);
  }
  }
    $msg = "<b>😃Hey $fname $lname Welcome To  Bot\n\n😏Join Our Channel\n\n👉 $channel\n\n😏After Joining Click Check Button</b>";

	keyboard($from_id, $msg, [[["text" => "💡 Check"]]]);
}
  if($text=='💡 Check'){
  action($from_id, "typing");
    $sts=joincheck($from_id, $channel);
    if(($sts=="member") || ($sts=="administrator") || ($sts=="creator")){
      
        $msgg= "<b>😃Hey $fname $lname Welcome To Main Menu</b>";

	keyboard($from_id, $msgg, [[["text" => "🔋 Balance"],["text"=>"🎁 Bonus"],["text"=>"🔭 Referral"]],[["text"=>"🔒 Wallet"],["text"=>"🏧  Payout"]],[["text"=>"📶 Bot Status"],["text"=>"🎟️  Bot Info"]]]);
    }else{
  $msg = "<b>😃 Hey $fname $lname Welcome To Bot\n\n😏Join Our Channel\n\n👉 $channel \n\n😏After Joining Click Check Button</b>";

	keyboard($from_id, $msgg, [[["text" => "💡 Check"]]]);
    }
  }
    if($text=="🔋 Balance"){
      $bal=file_get_contents("Admin/balance/$from_id.txt");
      Message($from_id, "<b>👤 Name : $fname\n\n🆔 User ID : $from_id \n\n💵 Balance: $bal.0Rs\n\nBot Developer: @Mohd_arman_idrisi01</b>");
    }
      if($text=="🔭 Referral"){
        Message($from_id, "<b>🔎Welcome To Invite Section\n\n📇 Your Invite Link:https://t.me/$botusername?start=$from_id\n\n💴 Invite Your Friends And Earn $per_refer Cash</b>");
      }
        if($text=="🔒 Wallet"){
          $wal=file_get_contents ("Admin/wallet/$from_id.txt");
          if($wal==""){
            $wal="not set";
          }
Message($from_id, "<b>🔍 User: $fname $lname\n\n✅️ currently Paytm wallet Set To: $wal\n\n⚡️ For Set Wallet Send Like This</b>: <code>/setwallet paytm_number</code>");
        }
          if($text =="📶 Bot Status"){
        $po=file_get_contents ("Admin/total/payout.txt");
         $usrs=file_get_contents("Admin/total/users.txt");
         Message($from_id,"<b>📊 BOT LIVE STATS 📊\n\n📤 TOTAL PAYOUTS : $po.0 INR\n\n💡 TOTAL USERS: $usrs USERS\n\n🔎 CODED BY : Arman Idrisi !</b>");
          }
            if($text=="🎁 Bonus"){
              Message($from_id, "<b>❌️ Bonus Is Not Avalaible</b>");         }
    if ($text == "/setwallet" or $a=substr($text, 0, 10) == "/setwallet") {
  $ids = explode("/setwallet ",$text);   
  $id = $ids[1];
      if($id==""){Message($from_id, "Send Like this /setwallet your_paytm_number");}else{
if(strlen ($id)==10){
           Message($from_id, "<b>✅️ Paytm Number Is Set to: </b><code>$id $type</code>");
  file_put_contents("Admin/wallet/$from_id.txt",$id);
}else{
  Message($from_id, "<b>❌️ Please Send Valid 10 Digit Number</b>");
           }

      }
    }
if($text=="🎟️  Bot Info"){
  Message($from_id, "<b>this Bot Create By @Mohd_arman_idrisi01 In Php Server \n\n subscribe On youtube youtube.com/@armanidrisi1</b>");
}
  if($text=="🏧  Payout"){
    Message($from_id, "<b>Send Like This</b>\n\n<code>/withdraw 1</code>" );
  }
    if ($text == "/withdraw" or substr($text, 0,9) == "/withdraw") {
  $ids = explode("/withdraw ",$text);
  $amo = $ids[1];
      $bal=file_get_contents ("Admin/balance/$from_id.txt");
      if(($amo<$min_withdraw) || ($amo>$max_withdraw)){
        Message($from_id, "<b>⛔️ Invalid Amount \n\n Minimum Withdraw Is $min_withdraw And Maximum Withdraw Is $max_withdraw</b>");
      }else{
        if($bal<$amo){
          Message($from_id, "⛔️ <b>Enterred Amount Is Greater Than Your Balance</b>");
        }else{
          Message($from_id, "🕛 Processing Your Withdraw.....");
          $mob=file_get_contents ("Admin/wallet/$from_id.txt");
            $api="https://full2sms.in/api/v1/disburse/paytm?mid=$mid&mkey=$mkey&guid=$guid&amount=$amo&mobile=$mob&info=$comment";
$res=file_get_contents ($api);
Message($from_id, "<b>Result: $res</b>");
          $stats=file_get_contents("Admin/total/payout.txt");
          file_put_contents("Admin/total/payout.txt", $stats+$amo);
file_put_contents ("Admin/balance/$from_id.txt",$bal-$amo);  
        }
      }
}
?>