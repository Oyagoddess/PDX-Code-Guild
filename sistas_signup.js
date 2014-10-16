$(document).ready(function() {
    $("#sign-up").click(
        function () {
            var welcome = alert("Welcome to SISTAS Connection");
            var sign_up = prompt('Would you like to sign up? type yes or no');

            if (sign_up === "yes") {
                    alert("Sorry, our site is not ready yet, but please look around and check back soon");
            }
            else {
                alert("Feel free to look around");
           }
    });
//      working to create a hover function for photo
//    $("#celebrate").hover(
//        function () {
//            $(this).attr({src:"http://aspiretoyou.com/wp-content/uploads/2011/08/women-empowerment.jpg"});
//        function () {
//            $(this).attr({src: "http://my.clevelandclinic.org/ccf/media/Images/celebrate-sisterhood/celebrate-sisterhood-header2.jpg"})
//        }
//        })
});
//var test = document.getElementById("sign-up");
//console.log(test);
