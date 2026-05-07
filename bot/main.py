<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Movie Mini App</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body { background: #1a1a1a; color: white; font-family: sans-serif; padding: 20px; }
        .movie { background: #333; padding: 15px; border-radius: 10px; margin-bottom: 10px; display: flex; justify-content: space-between; }
        .btn { background: #2481cc; color: white; border: none; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <h2>🎬 Yangi Kinolar</h2>
    <div class="movie">
        <div>
            <strong>Oppenheimer</strong><br><small>Reyting: 8.9</small>
        </div>
        <button class="btn" onclick="watch(1)">Ko'rish</button>
    </div>
    <script>
        const tg = window.Telegram.WebApp;
        tg.expand();
        function watch(id) {
            tg.sendData(JSON.stringify({action: 'watch', id: id}));
        }
    </script>
</body>
</html>
