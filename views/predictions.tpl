<html>
    <head>
        <meta charset="UTF-8">
        <title> My first Web-Page </title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
              rel="stylesheet"
              integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
              crossorigin="anonymous"
        />
        <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js"></script>
    </head>
    <body>
        <h1> Сегодня {{ date }} </h1>

        <p> {{ predictions }} </p>
        <br/>
        <hr/>
        <a href="about.html"> About us </a>
        &nbsp;
        <a href="contacts.html"> Contacts </a>
        <p>Copyright Andrei &copy;</p>
    </body>
    <script>
        console.log({{x}})
    </script>
</html>