var SpeechRecognition = window.webkitSpeechRecognition;
  
var recognition = new SpeechRecognition();

var instructions = $('instructions');

var Content = '';

recognition.continuous = true;

recognition.onresult = function(event) {

  var current = event.resultIndex;

  var transcript = event.results[current][0].transcript;
 
    Content = transcript;

    if (Content.includes('sign in'))
    {
        window.open('/SignIn');
    }

    else if (Content.includes('sign up'))
    {
        window.open('/SignUp');
    }

    else if (Content.includes('log in'))
    {
        window.open('/LogIn');
    }

    else if (Content.includes('log out'))
    {
        window.close();
        window.open('/LogOut');
    }

    else if (Content.includes('register'))
    {
        window.open('/Register');
    }

    else if (Content.includes('prediction'))
    {
        window.open('/PredictStocks');
    }

    else if (Content.includes('game stats') || Content.includes('paladins stats'))
    {
        window.open('https://paladins.guru/profile/16622935-bravoshka');
        window.open('https://paladins.guru/profile/714214141-Nasreen');
    }

    else if (Content.includes('musharaf stats') || Content.includes("musharaf's stats") || Content.includes('best player') || Content.includes('legend') || Content.includes('champion'))
    {
        window.open('https://paladins.guru/profile/16622935-bravoshka');
    }
    
    else if (Content.includes('mohsin stats') || Content.includes("mohsin's stats") || Content.includes('average' ))
    {
        window.open('https://paladins.guru/profile/714214141-Nasreen');
    }
    
    else if (Content.includes('zain stats') || Content.includes("zain's stats") || Content.includes('mediocre' ))
    {
        window.open('https://paladins.guru/profile/718038281-huhuhahaaaa0');
    }

    else if (Content.includes('saad stats') || Content.includes("saad's stats")  || Content.includes('pathetic' ))
    {
        window.open('https://paladins.guru/profile/718038281-huhuhahaaaa0');
    }

  
};

recognition.onstart = function() { 
  instructions.text('Voice recognition is ON.');
}

recognition.onspeechend = function() {
  instructions.text('No activity.');
}

recognition.onerror = function(event) {
  if(event.error == 'no-speech') {
    instructions.text('Try again.');  
  }
}

$('#start-btn').on('click', function(e) {
  recognition.start();
});
