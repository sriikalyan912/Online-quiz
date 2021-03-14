var q_no = 1;

myfunction = () => {
    var option = document.getElementsByName(q_no);
    for(var i = 0; i<4; i++){
        if(option[i].checked){
            break;
        }
    }
    ChechAnswer(option[i].value)

    var option_class = document.getElementsByClassName('options')[0].style.pointerEvents = 'none';
    console.log(option_class)
    
}

ChechAnswer = (value) => {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var a = JSON.parse(this.responseText)
            if(a["is_correct"]){
                document.getElementById(`option_${value}-Box`).style.backgroundColor = 'rgb(11, 212, 145)';
        
            }
            else{
                document.getElementById(`option_${value}-Box`).style.backgroundColor = 'red';
            }
            
        };
    };

    console.log('hello')

    xhttp.open('GET', window.location.href+'/'+value , true);
    xhttp.send();

    
    console.log(quiz_name)
};