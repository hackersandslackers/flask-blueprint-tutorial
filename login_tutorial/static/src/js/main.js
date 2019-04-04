// Remove Alert on Close

var alertbutton = document.querySelector('.alert button');

if (alertbutton){
  alertbutton.addEventListener('click', function (event) {

  	// If the clicked element doesn't have the right selector, bail
  	if (!event.target == alertbutton) return;
    alertbutton.parentNode.style.display = 'none';

  	// Don't follow the link
  	event.preventDefault();

  }, false);
}
