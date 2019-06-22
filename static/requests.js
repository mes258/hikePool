function getRide(rideId) {
  $.ajax({
    url: '/getRide',
    method: 'POST',
    data: {
      'rideId': ''
    }
  }).done(function(result) {
    console.log(result);
  }).fail(function() {
    console.log('AJAX error');
  });
}

function getAllRides() {
  $.ajax({
    url: '/getRides',
    method: 'POST',
    data: {}
  }).done(function(result) {
    console.log(result);
  }).fail(function() {
    console.log('AJAX error');
  });
}

function getAllRequests() {
  $.ajax({
    url: window.location.href + '/getRequests',
    method: 'POST',
    data: {}
  }).done(function(result) {
    console.log(result);
  }).fail(function() {
    console.log('AJAX error');
  });
}
