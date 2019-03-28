
  	document.getElementById("submit_button").addEventListener("click", function(event){
  		var user = document.getElementById("email").value;
  		var pass = document.getElementById("password").value;
  		if(user == "" || pass == ""){
             alert("Please Enter Correct Credentials");

  		  event.preventDefault()
	  
	  
    }else{
     alert("Please Correct Credentials");
   }
   });

