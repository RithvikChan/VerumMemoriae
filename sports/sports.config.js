exports.url = "http://localhost:7878/sports/index.html";

// Returns a visual state that represents the given sport. 
function getStateFor(sportName) {
  return {
    check: function() {
      // Check that the sport is displayed.
      var main = document.getElementById('main');
      var sportDiv = main.children[main.children.length - 1];
      return sportDiv.getElementsByTagName('h1')[0].innerText.trim() === sportName;
    },
    next: function() {
      // Navigate to the next sport.
      document.getElementById('next').click();
    }
  };
}

exports.loop = ['Football', 'Handegg', 'Ultimate Frisbee', 'Quidditch'].map(getStateFor);
