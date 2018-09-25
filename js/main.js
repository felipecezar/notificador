{

/* ========================
    Inicialização Firebase
======================== */

var config = {
    apiKey: "AIzaSyBl9KWZ0hW-rTumxtx-SSb0Vv6aEV3mFTw",
    authDomain: "notificacoes-felipe.firebaseapp.com",
    databaseURL: "https://notificacoes-felipe.firebaseio.com",
    projectId: "notificacoes-felipe",
    storageBucket: "notificacoes-felipe.appspot.com",
    messagingSenderId: "510362805881"
  };
  firebase.initializeApp(config);



/* ========================
    Variáveis
======================== */

const FIREBASE_AUTH = firebase.auth();
const FIREBASE_MESSAGING = firebase.messaging();
const FIREBASE_DATABASE = firebase.database();

const btnLogar = document.getElementById('logar');
const btnSair = document.getElementById('sair');
const btnInscrever = document.getElementById('inscrever');
const btnDesinscrever = document.getElementById('desinscrever');

const toast = document.getElementById("toast");
const toast_titulo = document.getElementById("toast-titulo");
const toast_corpo = document.getElementById("toast-corpo");
const toast_icone = document.getElementById("toast-icone");


/* ========================
    Eventos
======================== */

btnLogar.addEventListener('click', logar);
btnSair.addEventListener('click', sair);
btnInscrever.addEventListener('click', inscrever);
btnDesinscrever.addEventListener('click', desinscrever);


FIREBASE_AUTH.onAuthStateChanged(estadoAutenticacaoAlterado);


FIREBASE_MESSAGING.onMessage((payload)=>{

    toast_corpo.innerHTML = payload.data.title + " : "+ payload.data.body;
    toast_icone.innerHTML = "<img src=\"https://pbs.twimg.com/profile_images/1532886460/He-man_400x400.jpg\" width=\"50px\" height=\"50px\">";

    toast.className = "show";
    
    setTimeout(()=>{
        toast.className = toast.className.replace("show", ""); 
        }, 5000);
   
})


/* ========================
    Funções 
======================== */

function logar(){
    FIREBASE_AUTH.signInWithPopup( new firebase.auth.GoogleAuthProvider() );
}

function sair(){
    FIREBASE_AUTH.signOut();
}

function estadoAutenticacaoAlterado(usuario) {
    if(usuario){
        console.log(usuario);

        btnLogar.setAttribute('hidden','true');
        btnSair.removeAttribute('hidden');

        checarInscricao();

    } else {
        console.log('Ningem logado');

        btnSair.setAttribute('hidden','true');
        btnLogar.removeAttribute('hidden');
    }
}

function inscrever(){
    FIREBASE_MESSAGING.requestPermission()
        .then(()=> atualizarTokenBD())
        .then(()=> checarInscricao())
        .catch(()=> console.log('Usuario é prosa e ainda não se increvel.'));
}

function desinscrever(){
    FIREBASE_MESSAGING.getToken()
        .then((token)=> FIREBASE_MESSAGING.deleteToken(token))
        .then(()=> FIREBASE_DATABASE.ref('/tokens').orderByChild('uid').equalTo(FIREBASE_AUTH.currentUser.uid).once('value'))
        .then((snapshot)=> {
            console.log(snapshot.val());
            const key = Object.keys(snapshot.val())[0];
            return FIREBASE_DATABASE.ref('/tokens').child(key).remove();
        })
        .then(()=> checarInscricao())
        .catch(()=> console.log('Falha ao desinscrever.'));
}

function atualizarTokenBD(){
    return FIREBASE_MESSAGING.getToken()
        .then((token)=> {
            FIREBASE_DATABASE.ref('/tokens').push({
                token: token,
                uid: FIREBASE_AUTH.currentUser.uid
            });
        });
}

function checarInscricao(){
    FIREBASE_DATABASE.ref('/tokens').orderByChild('uid').equalTo(FIREBASE_AUTH.currentUser.uid).once('value')
        .then((snapshot)=>{
            if (snapshot.val()){
                btnInscrever.setAttribute('hidden','true');
                btnDesinscrever.removeAttribute('hidden');
            }else {
                btnDesinscrever.setAttribute('hidden','true');
                btnInscrever.removeAttribute('hidden');
            }
        })
}

}