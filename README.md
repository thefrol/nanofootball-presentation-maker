# Создатель презентаций Nanofootball

Формирует из `dict` объекта презентацию, которую можно отправить клиенту. Требует около трех секунд на одно упражнение. Таким образом создание презентации из шесть упражнения займет 10-20 секунд

# Установка

    pip install nf_presentation

# Использование

    from nf_presentation import create_pptx

    create_pptx(input_data=training_data_dict,output_file='output.pptx')

И далее `output.pptx` можно отправлять уже пользователям

## Использование потока вместо временных файлов

Вместо того, чтобы создавать временный файл, функция `create_pptx` может писать в сразу в поток, который затем можно отправить по сети. 

    import io
    from nf_presentation import create_pptx

    with io.BytesIO() as f:
        create_pptx(input_data=training_data_dict, output_file=f)
        send_file(f)  # your server response to client
    

# Тестовые данные

В пакет встроенны тестовые данные, так то работоспособность пакета можно проверить так:


    from nf_presentation import create_from_test_data

    create_from_test_data(output_file='output.pptx')

Вместо временного файла можно так же использовать поток, как в примере выше

        with io.BytesIO() as f:
            create_from_test_data(output_file=f)
            send_file(f)  # your server response to client

## TODO

1. Настроить логгер вместо print(..)
1. + Устранить утечку памяти где создается поток для объектак. Используя with
2. + Презентация в широком формате
3. + Новое форматирование 
4. Описание сделал читабельным
5. Капитализация значений в левой таблице
6. Размер шрифта, положение в строке
7. + Форматирование в шаблоне двухконтентном
8. + Цвета?
9. Cоздать презентацию для каждого упражнения, дабы отловить возможные ошибки

## Текущие проблемы

Некоторые схемы получаются искаженными, даже в упражнении из тестовых данных. Там одни из ворот почему-то вытянуты по диагонали. Слава богу, в похожей схеме из другого упражнения все нормально. Так что сравнив схемы там и там, можно решить проблему

В данный момент изображения создаются из других изображений(ворот, игроков и прочее). И эти ворота игроки скачиваются из интернета. Было бы неплохо, если бы можно было искать эти файлы локально, на сервере. Это помогло бы ускорить процесс. 

### Битый SVG

В аттрибуте shchemeData упражения хранится svg фай схемы. Можно было бы легко пользоваться этими свг, и переделать их в пнг. Но есть проблема. Эти SVG битые. 

Аттрибуты записаны некорректно. То есть с точки зрения браузера они написаны верно, а с точки зрения форматирования svg - нет. Дело в том, что для браузера не существует различий между прописными с строчными буквами, например viewBox и viewbox для браузера выглядят одинаково, но для любой программы читающей изображения(в том числе cairoSVG) viewbox без большой буквы будет считаться ошибкой и пропущен обработчиком.

Поэтому важно поправить данные полях схем, перед передачей в субпрограмму, которая из этой свг сделает PNG
> При обработке SVG данных из schemeData упражнения будут сделаны такие замены
> 1. viewbox -> viewBox
> 2. markerwidth -> markerWidth
> 3. refx -> refX
> 4. ...
> 
> Все такие замены набиваются руками и лежат в nf_presentation.settings.svg_replacements
> так же можно воспользоваться фукцией nf_presentation.settings.add_svg_replacement(old,fix), чтобы добавить новую подстановку. Потому что в дальнейшем список таких замен будет только расширяться, и если картинка на выходе не совсем походит на ту, что на сайте, скорее всего нужно поправить какой-то битый аттрибут.



### Зависимости SVG

В каждой картинке схемы из базы данных хранится ссылки на другие файлы, к счастью CairoSVG может использовать веб ссылки для картинок, чтобы создать потом png файл

> При обрботке svg схемы все ссылки /static/schemeDrawer/img/... будут заменяться на http://nanofootball.com/static/schemeDrawer/img/...
> 
> Подразумевается что все картинки доступны по адресу http://nanofootball.com/static/schemeDrawer/img/...

### Зависимости перекодировщика SVG -> PNG 

Модуль cairosvg, который собсно и перегружает картинки имеет в зависимостях cairocffi, которые на виндоус надо устанавливать отдельно, а в линуксе пока вообще хз что. Кажется это довольно грузная зависимость для сервера NF

> В данный момент подразумевается, что при установке пакета nf-presentation устанавливается CairoSVG, которая в свою очередь автоматически установит cairocffi на линкус систему. Подразумевается, что наш НФ сервер работает на линуксе