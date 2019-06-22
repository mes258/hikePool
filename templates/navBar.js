document.getElementById("navMenu").innerHTML =
'<a class="navbar-brand" href="{{url_for(\'index\')}}">Hitch A Ride</a>' + 
'<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">' +
    '<span class="navbar-toggler-icon"></span>' + 
'</button>' +
'<div class="collapse navbar-collapse" id="navbarNav">'+
    '<ul class="navbar-nav">'+
        '<li class="nav-item"> <a class="nav-link" href="{{url_for(\'viewRides\')}}">View Rides</a> </li>' +
        '<li class="nav-item"> <a class="nav-link" href="{{url_for(\'drivers\')}}">Add a Ride</a> </li>' +
        '<li class="nav-item"> <a class="nav-link active" href="{{url_for(\'riders\')}}">Join a Ride</a> </li>' +
        '<li class="nav-item"> <a class="nav-link" href="{{url_for(\'faq\')}}">FAQ</a> </li>' +
        '<li class="nav-item"> <a class="nav-link" href="{{url_for(\'privacy\')}}">Privacy</a> </li>' +
    '</ul>' +
'</div>';