importScripts("https://www.gstatic.com/firebasejs/5.3.1/firebase-app.js")
importScripts("https://www.gstatic.com/firebasejs/5.3.1/firebase-messaging.js")

var config = {
    apiKey: "AIzaSyBl9KWZ0hW-rTumxtx-SSb0Vv6aEV3mFTw",
    authDomain: "notificacoes-felipe.firebaseapp.com",
    databaseURL: "https://notificacoes-felipe.firebaseio.com",
    projectId: "notificacoes-felipe",
    storageBucket: "notificacoes-felipe.appspot.com",
    messagingSenderId: "510362805881"
  };

firebase.initializeApp(config);

const messaging = firebase.messaging();

messaging.setBackgroundMessageHandler((playload)=>{
    console.log(playload);
    const titulo = playload.data.title;
    const opcoes = {
        body: playload.data.body,
        icon: 'https://pbs.twimg.com/profile_images/1532886460/He-man_400x400.jpg'
    };

    return self.registration.showNotification(titulo, opcoes);
});