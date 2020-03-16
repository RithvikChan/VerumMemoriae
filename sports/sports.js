var main = document.getElementById('main');
var next = document.getElementById('next');
var prev = document.getElementById('prev');

var currentSport = null;
// apologies in advance to sports fans.
var sports = [{
  name: 'Football',
  description: 'Football is a sport in which players kick a ball around a field.'
}, {
  name: 'Handegg',
  description: 'Handegg, sometimes mistakenly called football, is a sport in which players throw an egg-shaped ball. Players kick the ball in a limited set of circumstances.'
}, {
  name: 'Ultimate Frisbee',
  description: "It's a weird combination of basketball pass rules (without dribbling) and football scoring rules, but with a frisbee."
}, {
  name: 'Quidditch',
  description: "Quidditch is a sport where the points don't really matter at all; entire games rest on the shoulders of a single player from each team."
}];
// Array memory leak: Nothing manages the size of this array.
var sportVisitHistory = [];

function presentSport(sport) {
  var div = document.createElement('div');
  div.className = "sport";
  div.innerHTML = "<h1>" + sport.name + "</h1><p>" + sport.description + "</p>";
  main.appendChild(div);
}

function selectSport(newSport, addToHistory) {
  // Hide previous sports.
  // DOM memory leak: Doesn't remove sports from the GUI!
  var divs = document.getElementsByClassName('sport');
  for (var i = 0; i < divs.length; i++) {
    divs[i].style.display = "none";
  }
  if (addToHistory) {
    sportVisitHistory.push(currentSport);
  }
  currentSport = newSport;
  presentSport(currentSport);
}

function nextSport() {
  var oldSport = currentSport;
  if (oldSport !== null) {
    // Causes bug: Prev only works once.
    // Causes memory leak: Click handlers keep getting added and are never removed.
    prev.addEventListener('click', function() {
      selectSport(oldSport, false);
    });
  }
  var newIndex = sports.indexOf(currentSport) + 1;
  if (newIndex >= sports.length) {
    newIndex = 0;
  }
  selectSport(sports[newIndex], true);
}

next.addEventListener('click', nextSport);

nextSport();
