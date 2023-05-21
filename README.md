# PyNOSQL


    (_)         (_)         (_)         (_)         (_)         (_)   
    (_)         (_)         (_)         (_)         (_)         (_)   
    (_)_       _(_)         (_) _  _  _ (_)         (_)_       _(_)   
      (_)     (_)           (_)(_)(_)(_)(_)           (_)     (_)     
       (_)   (_)     _  _   (_)         (_)  _  _      (_)   (_)      
        (_)_(_)     (_)(_)  (_)         (_) (_)(_)      (_)_(_)       
          (_)       (_)(_)  (_)         (_) (_)(_)        (_)    

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=40&pause=1000&color=F70000&center=true&vCenter=true&width=435&lines=PyNOSQL)](https://git.io/typing-svg)

<div>
<h1>MongoDB_RabbitMQ_Contact</h1>

<h2>Встановлення</h2>
<p>Встановіть Python 3.8 або новіший, MongoDB та RabbitMQ.</p>

<p>Клонуйте цей репозиторій:</p>

    git clone https://github.com/VAlduinV/PyNOSQL.git

<h2>Використання</h2>
<p>Запустіть producer.py для генерації контактів та відправки їх в чергу RabbitMQ:</p>
    
    python producer.py

<p>Запустіть consumer_sms.py або consumer_email.py для отримання контактів з черги та імітації надсилання повідомлень:</p>

    python consumer_sms.py
    python consumer_email.py

<h2>Моделі даних</h2>
<p>Проект використовує MongoDB для зберігання контактів. Кожний контакт має наступні поля:</p>
<ul>
    <li>full_name: Повне ім'я контакту. Обов'язкове поле.</li>
    <li>email: Email контакту. Обов'язкове поле.</li>
    <li>phone: Телефонний номер контакту. Не обов'язкове поле.</li>
    <li>message_sent: Логічне поле, яке показує, чи було надіслано повідомлення контакту. Значення за замовчуванням - False.</li>
</ul>
<p>Інтеграція з RabbitMQ</p>
<p>Цей проект використовує RabbitMQ для організації черги повідомлень. Кожен контакт, що потребує надсилання повідомлення, відправляється в одну з двох черг: sms_queue для SMS-повідомлень та email_queue для email-повідомлень.</p>
</div>