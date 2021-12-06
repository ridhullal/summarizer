function countWord() {
 
            
            var words = document
                .getElementById("input-textarea").value;
                
    
            var count = 0;
 
            
            var split = words.split(' ');
 
            
            for (var i = 0; i < split.length; i++) {
                if (split[i] != "") {
                    count += 1;
                }
            }
 
            console.log(count)
            document.getElementById("inputcount").innerHTML = count;
        }

function countWordOutput() {
 
            
            var words = document
                .getElementById("output-textarea").value;
                
    
            var count = 0;
 
            
            var split = words.split(' ');
 
            
            for (var i = 0; i < split.length; i++) {
                if (split[i] != "") {
                    count += 1;
                }
            }
 
            console.log(count)
            document.getElementById("outputcount").innerHTML = count;
        }

function myCopyFunction() {
  var copyText = document.getElementById("output-textarea");

  copyText.select();
  copyText.setSelectionRange(0, 99999); 

  
  navigator.clipboard.writeText(copyText.value);
  
  
  
}

    