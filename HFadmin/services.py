from hashlib import md5
from django.db.models import F
from django.utils.safestring import mark_safe
from HFhtml.models import Users
from django.db.models.functions import Right, MD5
from django.core.mail import send_mail
from HappyFamily.settings import EMAIL_HOST_USER


def send_email(user, email, subject):
    """ Отправка письма при регистрации, письма со ссылкой для смены пароля, письма об успешной смене пароля """
    message, subject_text = "", ""
    if subject == 'reset':
        message = "<!DOCTYPE " \
                  "html>" \
                  "<html " \
                  "lang=\"en\">" \
                  "<head>" \
                  "<link rel=\"icon\" href=\"https://hf86.ru/img/logo.ico\">" \
                  "<meta charset=\"UTF-8\">" \
                  "<title>Happy " \
                  "Family " \
                  "Surgut </title>" \
                  "<link rel =\"stylesheet\" href=\"https://use.fontawesome.com/releases/v5.3.1/css/all.css\" " \
                  "integrity=\"sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU\" " \
                  "crossorigin=\"anonymous\">" \
                  "</head>" \
                  "<body>" \
                  "<table " \
                  "width =\"100%ds\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td " \
                  "align =\"center\" valign=\"top\">" \
                  "<table " \
                  "width =\"640\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td " \
                  "align =\"center\" valign=\"top\" width=\"600\">" \
                  "<table " \
                  "width =\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td " \
                  "align =\"left\" valign=\"top\" height=\"15\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  "align =\"left\" valign=\"top\">" \
                  "<table " \
                  "width =\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td " \
                  "align =\"left\" valign=\"top\" width=\"95\" height=\"36\"><a href=\"https://hf86.ru\" " \
                  "target=\"_blank\"><img src=\"https://hf86.ru/img/logo.png\" width=\"95\" " \
                  "style=\"display:block;\" " \
                  "border=\"0\" alt=\"Happy Family\"></a>" \
                  "</td>" \
                  "<td " \
                  "align =\"right\" valign=\"middle\" style=\"font-family:Arial, Helvetica, " \
                  "sans-serif;font-size:12px;line-height:15px;color:#585858;\">" \
                  "HAPPY " \
                  "FAMILY " \
                  "SURGUT" \
                  "</td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  "align =\"left\" valign=\"top\" height=\"25\">" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  "align =\"left\" valign=\"top\" style=\"border:1px solid #dddddd;\" bgcolor=\"#ffffff\">" \
                  "<table " \
                  "width =\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td " \
                  "align =\"left\" valign=\"top\" width=\"49\">" \
                  "</td>" \
                  "<td " \
                  "align =\"left\" valign=\"top\" width=\"500\">" \
                  "<table " \
                  "width =\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td " \
                  "align =\"left\" valign=\"top\" height=\"50\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  " align =\"left\" valign=\"top\" style=\"font-size:22px;line-height:28px;color:#333333;font-weight" \
                  f":bold;font-family:Arial, Helvetica, sans-serif;\">Привет {user[0]['email']},</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  "height =\"20\" align=\"left\" valign=\"top\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  "align =\"left\" valign=\"top\" style=\"font-size:14px;line-height:19px;color:#585858;font-family" \
                  ":Arial, Helvetica, sans-serif;\">" \
                  "Для " \
                  "смены " \
                  "пароля " \
                  "на " \
                  "сайте <a " \
                  "href =\"https://hf86.ru\" target=\"_blank\" style=\"text-decoration:none;color:#585858;\"><span " \
                  "style=\"text-decoration:none;color:#585858;\">hf86.ru</span></a>." \
                  "<br><br>" \
                  "Нажмите " \
                  "на " \
                  "кнопку " \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  "height =\"25\" align=\"left\" valign=\"top\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  "align =\"left\" valign=\"top\" height=\"50\">" \
                  "<table " \
                  "width =\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td " \
                  "align =\"left\" valign=\"top\" width=\"126\"></td>" \
                  "<td " \
                  "align =\"center\" valign=\"middle\" height=\"50\" width=\"248\" bgcolor=\"#0082b2\" " \
                  "style=\"font-size:14px;line-height:19px;color:#ffffff;font-family:Arial, Helvetica, " \
                  f"sans-serif;\"><a href=\"https://hf86.ru/enter/?forget={user[0]['reset']}\" target=\"_blank\" " \
                  "style=\"color:#ffffff;text-decoration:none;\"><span " \
                  "style=\"font-size:14px;line-height:19px;color:#ffffff;font-family:Arial, Helvetica, " \
                  "sans-serif;\">СМЕНИТЬ ПАРОЛЬ</span></a></td>" \
                  "<td " \
                  "align =\"left\" valign=\"top\" width=\"126\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  "height =\"25\" align=\"left\" valign=\"top\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  "align =\"left\" valign=\"top\" style=\"font-size:14px;line-height:19px;color:#585858;font-family" \
                  ":Arial, Helvetica, sans-serif;\">Или скопируйте данную строку в браузер:<br>" \
                  "<a " \
                  f"href =\"https://hf86.ru/enter/?forget={user[0]['reset']}\" target=\"_blank\" " \
                  "style=\"text-decoration: none;color:#0082b2;\"><span " \
                  f"style=\"color:#0082b2;\">https://hf86.ru/enter/?forget={user[0]['reset']}</span></a>" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  "height =\"30\" align=\"left\" valign=\"top\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  "height =\"30\" align=\"left\" valign=\"top\" style=\"border-top:1px solid #dddddd;\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  "align =\"left\" valign=\"top\" style=\"font-size:14px;line-height:19px;color:#585858;font-family" \
                  ":Arial, Helvetica, sans-serif;\">Спасибо, что Вы выбрали <a href=\"https://hf86.ru\" " \
                  "target=\"_blank\" style=\"text-decoration:none;color:#585858;\"><span " \
                  "style=\"text-decoration:none;color:#585858;\">hf86.ru</span></a>. Удачи!<br><br>" \
                  "<strong> С уважением, команда Happy Family </strong>" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align =\"left\" valign=\"top\" height=\"50\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "<td align =\"left\" valign=\"top\" width=\"49\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align =\"left\" valign=\"top\" height=\"40\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "<td align =\"center\" valign=\"top\" width=\"20\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "<table width =\"640\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td " \
                  "align =\"center\" valign=\"top\" width=\"20\"></td>" \
                  "<td " \
                  "align =\"center\" valign=\"top\" width=\"600\">" \
                  "<table " \
                  "width =\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td " \
                  "align =\"center\" valign=\"top\"><a href=\"https://hf86.ru\" target=\"_blank\"><img " \
                  "src=\"https://hf86.ru/img/logo.png\" width=\"95\" border=\"0\" alt=\"Logo\"></a></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  "align =\"center\" valign=\"top\" \
                  style=\"font-size:14px;line-height:19px;color:#585858;font-family:Arial, Helvetica, sans-serif;\">" \
                  "Happy Family Surgut " \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  "align =\"left\" valign=\"top\" height=\"20\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  "align =\"center\" valign=\"top\">" \
                  "<table " \
                  "<table " \
                  "width =\"100%\" cellspacing=\"0\" cellpadding=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td " \
                  "align =\"center\" valign=\"top\" width=\"120\"></td>" \
                  "<td " \
                  "align =\"center\" valign=\"top\" width=\"30\">" \
                  "<a" \
                  "href =\"https://instagram.com/happyfamily_hmao\" title=\"Instagram\" style=\"color:blue\">" \
                  "<img " \
                  "src =\"https://hf86.ru/img/icons/instagram.png\" height=\"20\">" \
                  "</a>" \
                  "</td>" \
                  "<td " \
                  "align =\"center\" valign=\"top\" width=\"30\">" \
                  "<a " \
                  "href =\"https://vk.com/happyfamily_hmao\" title=\"VK\" style=\"color:blue\">" \
                  "<img " \
                  "src =\"https://hf86.ru/img/icons/vk.png\" height=\"20\">" \
                  "</a>" \
                  "</td>" \
                  "<td " \
                  "align =\"center\" valign=\"top\" width=\"120\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  "align =\"left\" valign=\"top\" height=\"30\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td " \
                  "align =\"center\" valign=\"top\" \
                  style=\"font-size:11px;line-height:16px;color:#585858;font-family:Arial, Helvetica, sans-serif;\">" \
                  "Copyright © 2020" \
                  "</td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "<td " \
                  "align =\"center\" valign=\"top\" width=\"20\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</body>" \
                  "</html>"
        subject_text = "Смена пароля Happy Family"
    if subject == 'signup':
        message = "<!DOCTYPE html>" \
                  "<html lang=\"en\">" \
                  "<head>" \
                  "<link rel=\"icon\" href=\"https://hf86.ru/img/logo.ico\">" \
                  "<meta charset=\"UTF-8\">" \
                  "<title>Happy Family Surgut</title>" \
                  "<link rel=\"stylesheet\" href=\"https://use.fontawesome.com/releases/v5.3.1/css/all.css\" " \
                  "integrity=\"sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU\" " \
                  "crossorigin=\"anonymous\">" \
                  "</head>" \
                  "<body>" \
                  "<table width=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td align=\"center\" valign=\"top\">" \
                  "<table width=\"640\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td align=\"center\" valign=\"top\" width=\"600\">" \
                  "<table width=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" height=\"15\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\">" \
                  "<table width=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" width=\"95\" height=\"36\"><a href=\"https://hf86.ru\" " \
                  "target=\"_blank\"><img src=\"https://hf86.ru/img/logo.png\" width=\"95\" " \
                  "style=\"display:block;\" border=\"0\" alt=\"Happy Family\"></a>" \
                  "</td>" \
                  "<td align=\"right\" valign=\"middle\" style=\"font-family:Arial, Helvetica, " \
                  "sans-serif;font-size:12px;line-height:15px;color:#585858;\">" \
                  "HAPPY FAMILY SURGUT" \
                  "</td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" height=\"25\">" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" style=\"border:1px solid #dddddd;\" bgcolor=\"#ffffff\">" \
                  "<table width=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  " <td align=\"left\" valign=\"top\" width=\"49\">" \
                  "</td>" \
                  "<td align=\"left\" valign=\"top\" width=\"500\">" \
                  "<table width=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  " <tr>" \
                  "<td align=\"left\" valign=\"top\" height=\"50\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" style=\"font-size:22px;line-height:28px;color:#333333;font" \
                  f"-weight:bold;font-family:Arial, Helvetica, sans-serif;\">Привет {email},</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td height=\"20\" align=\"left\" valign=\"top\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" style=\"font-size:14px;line-height:19px;color:#585858;font" \
                  "-family:Arial, Helvetica, sans-serif;\">" \
                  "Мы рады видеть Вас частью <a href=\"https://hf86.ru\" target=\"_blank\" " \
                  "style=\"text-decoration:none;color:#585858;\"><span " \
                  "style=\"text-decoration:none;color:#585858;\">hf86.ru</span></a>." \
                  "<br><br>" \
                  "Для входа на сайт нажмите кнопку." \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td height=\"25\" align=\"left\" valign=\"top\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" height=\"50\">" \
                  "<table width=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" width=\"126\"></td>" \
                  "<td align=\"center\" valign=\"middle\" height=\"50\" width=\"248\" bgcolor=\"#0082b2\" " \
                  "style=\"font-size:14px;line-height:19px;color:#ffffff;font-family:Arial, Helvetica, " \
                  "sans-serif;\"><a href=\"https://hf86.ru/enter/\" target=\"_blank\" " \
                  "style=\"color:#ffffff;text-decoration:none;\"><span " \
                  "style=\"font-size:14px;line-height:19px;color:#ffffff;font-family:Arial, Helvetica, " \
                  "sans-serif;\">ВОЙТИ</span></a></td>" \
                  "<td align=\"left\" valign=\"top\" width=\"126\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td height=\"30\" align=\"left\" valign=\"top\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td height=\"30\" align=\"left\" valign=\"top\" style=\"border-top:1px solid #dddddd;\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" style=\"font-size:14px;line-height:19px;color:#585858;font" \
                  "-family:Arial, Helvetica, sans-serif;\">Спасибо, что Вы выбрали <a href=\"http://hf86.ru\" " \
                  "target=\"_blank\" style=\"text-decoration:none;color:#585858;\" rel=\" noopener " \
                  "noreferrer\"><span style=\"text-decoration:none;color:#585858;\">hf86.ru</span></a>. " \
                  "Удачи!<br><br>" \
                  "<strong>С уважением, команда Happy Family</strong>" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" height=\"50\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "<td align=\"left\" valign=\"top\" width=\"49\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" height=\"40\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "<td align=\"center\" valign=\"top\" width=\"20\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "<table width=\"640\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td align=\"center\" valign=\"top\" width=\"20\"></td>" \
                  "<td align=\"center\" valign=\"top\" width=\"600\">" \
                  "<table width=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td align=\"center\" valign=\"top\"><a href=\"http://hf86.ru\" target=\"_blank\"><img " \
                  "src=\"https://hf86.ru/img/logo.png\" width=\"95\" border=\"0\" alt=\"Logo\"></a></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"center\" valign=\"top\" style=\"font-size:14px;line-height:19px;color:#585858;font" \
                  "-family:Arial, Helvetica, sans-serif;\">" \
                  "Happy Family Surgut" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" height=\"20\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"center\" valign=\"top\">" \
                  "<table width=\"100%\" cellspacing=\"0\" cellpadding=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td align=\"center\" valign=\"top\" width=\"120\"></td>" \
                  "<td align=\"center\" valign=\"top\" width=\"30\">" \
                  "<a href=\"https://instagram.com/happyfamily_hmao\" title=\"Instagram\" style=\"color:blue\">" \
                  "<img src=\"https://hf86.ru/img/icons/instagram.png\" height=\"20\">" \
                  "</a>" \
                  "</td>" \
                  "<td align=\"center\" valign=\"top\" width=\"30\">" \
                  "<a href=\"https://vk.com/happyfamily_hmao\" title=\"VK\" style=\"color:blue\">" \
                  "<img src=\"https://hf86.ru/img/icons/vk.png\" height=\"20\">" \
                  "</a>" \
                  "</td>" \
                  "<td align=\"center\" valign=\"top\" width=\"120\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" height=\"30\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"center\" valign=\"top\" style=\"font-size:11px;line-height:16px;color:#585858;font" \
                  "-family:Arial, Helvetica, sans-serif;\">" \
                  "Copyright © 2020" \
                  "</td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "<td align=\"center\" valign=\"top\" width=\"20\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</body>" \
                  "</html>"
        subject_text = "Регистрация на сайте Happy Family"
    if subject == 'new_pass':
        message = "<!DOCTYPE html>" \
                  "<html lang=\"en\">" \
                  "<head>" \
                  "<link rel=\"icon\" href=\"https://hf86.ru/img/logo.ico\">" \
                  "<meta charset=\"UTF-8\">" \
                  "<title>Happy Family Surgut</title>" \
                  "<link rel=\"stylesheet\" href=\"https://use.fontawesome.com/releases/v5.3.1/css/all.css\" " \
                  "integrity=\"sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU\" " \
                  "crossorigin=\"anonymous\">" \
                  "</head>" \
                  "<body>" \
                  "<table width=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td align=\"center\" valign=\"top\">" \
                  "<table width=\"640\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td align=\"center\" valign=\"top\" width=\"600\">" \
                  "<table width=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" height=\"15\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\">" \
                  "<table width=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" width=\"95\" height=\"36\"><a href=\"https://hf86.ru\" " \
                  "target=\"_blank\"><img src=\"https://hf86.ru/img/logo.png\" width=\"95\" " \
                  "style=\"display:block;\" border=\"0\" alt=\"Happy Family\"></a>" \
                  "</td>" \
                  "<td align=\"right\" valign=\"middle\" style=\"font-family:Arial, Helvetica, " \
                  "sans-serif;font-size:12px;line-height:15px;color:#585858;\">" \
                  "HAPPY FAMILY SURGUT" \
                  "</td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" height=\"25\">" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" style=\"border:1px solid #dddddd;\" bgcolor=\"#ffffff\">" \
                  "<table width=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  " <td align=\"left\" valign=\"top\" width=\"49\">" \
                  "</td>" \
                  "<td align=\"left\" valign=\"top\" width=\"500\">" \
                  "<table width=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  " <tr>" \
                  "<td align=\"left\" valign=\"top\" height=\"50\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" style=\"font-size:22px;line-height:28px;color:#333333;font" \
                  f"-weight:bold;font-family:Arial, Helvetica, sans-serif;\">Привет {email},</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td height=\"20\" align=\"left\" valign=\"top\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" style=\"font-size:14px;line-height:19px;color:#585858;font" \
                  "-family:Arial, Helvetica, sans-serif;\">" \
                  "Вы только, что поменяли пароль на сайте <a href=\"https://hf86.ru\" target=\"_blank\" " \
                  "style=\"text-decoration:none;color:#585858;\"><span " \
                  "style=\"text-decoration:none;color:#585858;\">hf86.ru</span></a>." \
                  "<br><br>" \
                  "Для входа на сайт нажмите кнопку." \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td height=\"25\" align=\"left\" valign=\"top\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" height=\"50\">" \
                  "<table width=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" width=\"126\"></td>" \
                  "<td align=\"center\" valign=\"middle\" height=\"50\" width=\"248\" bgcolor=\"#0082b2\" " \
                  "style=\"font-size:14px;line-height:19px;color:#ffffff;font-family:Arial, Helvetica, " \
                  "sans-serif;\"><a href=\"https://hf86.ru/enter/\" target=\"_blank\" " \
                  "style=\"color:#ffffff;text-decoration:none;\"><span " \
                  "style=\"font-size:14px;line-height:19px;color:#ffffff;font-family:Arial, Helvetica, " \
                  "sans-serif;\">ВОЙТИ</span></a></td>" \
                  "<td align=\"left\" valign=\"top\" width=\"126\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td height=\"30\" align=\"left\" valign=\"top\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td height=\"30\" align=\"left\" valign=\"top\" style=\"border-top:1px solid #dddddd;\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" style=\"font-size:14px;line-height:19px;color:#585858;font" \
                  "-family:Arial, Helvetica, sans-serif;\">Спасибо, что Вы выбрали <a href=\"http://hf86.ru\" " \
                  "target=\"_blank\" style=\"text-decoration:none;color:#585858;\" rel=\" noopener " \
                  "noreferrer\"><span style=\"text-decoration:none;color:#585858;\">hf86.ru</span></a>. " \
                  "Удачи!<br><br>" \
                  "<strong>С уважением, команда Happy Family</strong>" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" height=\"50\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "<td align=\"left\" valign=\"top\" width=\"49\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" height=\"40\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "<td align=\"center\" valign=\"top\" width=\"20\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "<table width=\"640\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td align=\"center\" valign=\"top\" width=\"20\"></td>" \
                  "<td align=\"center\" valign=\"top\" width=\"600\">" \
                  "<table width=\"100%\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td align=\"center\" valign=\"top\"><a href=\"http://hf86.ru\" target=\"_blank\"><img " \
                  "src=\"https://hf86.ru/img/logo.png\" width=\"95\" border=\"0\" alt=\"Logo\"></a></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"center\" valign=\"top\" style=\"font-size:14px;line-height:19px;color:#585858;font" \
                  "-family:Arial, Helvetica, sans-serif;\">" \
                  "Happy Family Surgut" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" height=\"20\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"center\" valign=\"top\">" \
                  "<table width=\"100%\" cellspacing=\"0\" cellpadding=\"0\" border=\"0\">" \
                  "<tbody>" \
                  "<tr>" \
                  "<td align=\"center\" valign=\"top\" width=\"120\"></td>" \
                  "<td align=\"center\" valign=\"top\" width=\"30\">" \
                  "<a href=\"https://instagram.com/happyfamily_hmao\" title=\"Instagram\" style=\"color:blue\">" \
                  "<img src=\"https://hf86.ru/img/icons/instagram.png\" height=\"20\">" \
                  "</a>" \
                  "</td>" \
                  "<td align=\"center\" valign=\"top\" width=\"30\">" \
                  "<a href=\"https://vk.com/happyfamily_hmao\" title=\"VK\" style=\"color:blue\">" \
                  "<img src=\"https://hf86.ru/img/icons/vk.png\" height=\"20\">" \
                  "</a>" \
                  "</td>" \
                  "<td align=\"center\" valign=\"top\" width=\"120\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"left\" valign=\"top\" height=\"30\"></td>" \
                  "</tr>" \
                  "<tr>" \
                  "<td align=\"center\" valign=\"top\" style=\"font-size:11px;line-height:16px;color:#585858;font" \
                  "-family:Arial, Helvetica, sans-serif;\">" \
                  "Copyright © 2020" \
                  "</td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "<td align=\"center\" valign=\"top\" width=\"20\"></td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</td>" \
                  "</tr>" \
                  "</tbody>" \
                  "</table>" \
                  "</body>" \
                  "</html>"
        subject_text = "Смена пароля на сайте Happy Family"

    send_mail(subject=subject_text, from_email=EMAIL_HOST_USER, recipient_list=[email],
              html_message=message, message=message)


def get_error(txt):
    """ Возврат ошибки или сообщения """
    return mark_safe("<div class=\"m-alert m-alert--outline alert alert-danger alert-dismissible\" "
                     "role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" "
                     "aria-label=\"Close\"></button><span>" + txt + "</span></div>")


def create_user(email, password):
    """ Создание нового пользователя """
    return Users.objects.create_user(email=email, password=password)


def update_ref_counter(ref):
    """ Увеличение счетчика привлеченных пользователей на 1 для пользователя с указанным ref """
    Users.objects.annotate(email_md5=MD5('email')).annotate(ref_value=Right('email_md5', 8)).filter(
        ref_value=ref).values('ref').update(ref=F('ref') + 1)


def send_reset_pass(email):
    """ Проверка пользовтеля и отправка письма со ссылкой смены пароля """
    user = Users.objects.filter(email=email).values('email', 'reset')
    if user:
        send_email(user, email, 'reset')
        return get_error('На указанный email отправлено письмо с указаниями по смене пароля!')
    else:
        return get_error('Такого пользователя не существует')


def set_new_pass(email, password, forget):
    """ Установка пользователю нового пароля """
    user = Users.objects.filter(email=email, reset=forget)
    if user:
        _set_new_password(email, password)
        send_email('', email, 'new_pass')
        return {'auth_err': get_error('Пароль изменен. Пожалуйста авторизуйтесь')}
    else:
        return {'new_err': get_error('Такого пользователя не существует'), 'new': True}


def _set_new_password(email, password):
    """ Обновление пароля, ссылки для восстановления пароля в базе данных для пользователя с указанным email"""
    user = Users.objects.get(email=email)
    user.set_password(password)
    user.reset = str(md5(f"{email}{password}".encode()).hexdigest())
    user.save()
