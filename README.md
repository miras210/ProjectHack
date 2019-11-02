# 109SERVICE

**Telegram Bot that helps people**

    Input: 
        *Start* //button
         1) **Приветствие** // text
            Logo// image
        2) WAIT 2 seconds.
          Alert (text)
            REPLY phone, Fname and Lname (format: +7 *** *** ** **, text);   **PHONE CODE VERIFICATION** 
            IF NOT VERIFIED then *ERROR*
            
            #BUTTONS
            - Подача обращения
            - Проверка обращения
            - История обращений
            - Звонок в 109    Move to contacts
             
             [1] Подача обращения
             
             Choices
              1)Жалоба 
              2)Предложение
              3)Запрос 
              4)Заявление
              5)Отклик
                
             } список тем (extra) } выбор Гос.Учереждения(extra)
             
             1)Input text (memo)
             2)Input document (file)
             3) Conf. of input geo location (extra)
             4) confirm to send { YES or NO} if do not confirm then mo to the CHOICES.   ASK 'DOUBLE'
             5) OUTPUT: text, user number of choice, sending to SERVER
                 STATUS CHECK OUT!
                  BUTTON~~~ Проверить NUMBER обращения
                  
              [2] Проверка обращения
                    input: Обращение number
                    output: status: +++ ГОС.Учереждение+ ФИО исполнителя
                  STATUS:
                     1) Зарегистрирован
                     2) На расмотрении
                     3) Ответ доставлен заявителю\
                     4) Отклонено
               [3] История обращения
                   - список обращений: number of обращений + date
                   - Выбор обращения из списка and запрос его статуса.
                   
               [4] Информирование пользователей
                    Output: NEW INFO(message + image)
               [5] Звонок с телефона
                    Move to telephone / calling to 109
               
                   
               
            
 
