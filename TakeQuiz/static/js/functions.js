var question_no = 1;
const quiz_name = document.getElementById('quiz_name').innerText
const StartTime = new Date().getTime();


var score = 0;

nextQuestion = () => {

    question_no +=1 ;

    if(question_no >= 10){
        var FinishButton = document.getElementById('Next-Finish');
        FinishButton.innerText = 'Finish';
        FinishButton.onclick = function(){ FinishTest() };
    }

    document.getElementById('Next-Finish').disabled = true;
    document.getElementById('Next-Finish').style.backgroundColor = 'rgb(192, 150, 231)';

    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function(){

        if(this.readyState == 4 && this.status == 200){

           var Next_Question = JSON.parse(this.responseText);

           document.getElementById("Question").innerHTML =`${question_no}) `+ Next_Question['question']

           var reseter = document.getElementById('reseter');

           reseter.innerHTML = Next_Question_HTML(Next_Question);

           var option_class = document.getElementsByClassName('options')[0].style.pointerEvents = 'auto';
           
        };


    };

    xhttp.open('GET', `/takequiz/${ quiz_name }/test/${question_no}` , true);
    xhttp.send();


}

Next_Question_HTML = (content) =>{
    var new_HTML = '';
    
    var alps = ["A", "B", "C", "D"]

    alps.forEach(assign= (i)=>{
    new_HTML += `
    <li>
        <div class="option" id="option_${i}-Box">
            <h3>
                <input type="radio" name="${content['question_no']}" onchange="myfunction()" value="${i}" id="Option_${i}">${i}) ${content[`option_${i}`] }
            </h3>
        </div>
    </li>`});

    return new_HTML;
}

myfunction = () => {
    var option = document.getElementsByName(question_no);
    for(var i = 0; i<4; i++){
        if(option[i].checked){
            break;
        }
    }
    ChechAnswer(option[i].value)

    var option_class = document.getElementsByClassName('options')[0].style.pointerEvents = 'none';
    
}

ChechAnswer = (value) => {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var response = JSON.parse(this.responseText)
            if(response["is_correct"]){
                document.getElementById(`option_${value}-Box`).style.backgroundColor = 'rgb(11, 212, 145)';
                score += 1;
        
            }
            else{
                document.getElementById(`option_${value}-Box`).style.backgroundColor = 'rgb(235, 45, 45)';
                document.getElementById(`option_${response["Correct_option"]}-Box`).style.backgroundColor = 'rgb(11, 212, 145)';
            }
            document.getElementById('Next-Finish').disabled = false;

            document.getElementById('Next-Finish').style.backgroundColor = 'blueviolet';

            document.getElementById('Next-Finish').onmouseover = () =>{
                document.getElementById('Next-Finish').style.backgroundColor = 'rgb(106, 34, 173)';
            }
        };
    };

    console.log(window.location.href);
    xhttp.open('GET', window.location.href+question_no+'/'+value , true);
    xhttp.send();


};

FinishTest = () =>{
    var EndTest = new Date().getTime();
    var difference = EndTest - StartTime ; 
    var difference_in_seconds = Math.floor((difference % (1000 * 60))/ 1000)

    var minutes = Math.floor(difference_in_seconds/60)
    var seconds = Math.floor(difference_in_seconds % 60)

    var timetaken = minutes+":"+seconds
    console.log(window.location.href);
    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var result = JSON.parse(this.responseText)
            passfail = (result['score']/2)*100
            var status = 'FAIL'
            if(passfail >= 50){
                status = 'Pass'
            }
            
            
            document.getElementById('reseter').innerHTML = `
            <li>
                <h3>Student Name : ${result['student_name']}</h3>
            </li>
            <li>
                <h3>Quiz Name    : ${result['quiz_name']}</h3>
            </li>
            <li>
                <h3>Score        : ${result['score']}</h3>
            </li>
            <li>
                <h3>Time Taken   : ${result['timetaken']} mins:sec </h3>
            </li>
            <li>
                <h3>Status       : ${status}</h3>
            </li>
            `
            document.getElementById('student_name').innerHTML = '';
            document.getElementById('Question').innerHTML = '';

            var home = document.getElementById('Next-Finish')
            home.innerHTML = 'Home';
            home.onclick = function(){
                BackToHome()
            }
        };
    };

    student_name = document.getElementById('student_name').innerHTML;
    xhttp.open('GET', window.location.href+`finishtest/${student_name}/${score}&${timetaken}` , true);
    xhttp.send();

}

BackToHome = () => {
    window.location.assign(`${window.location.protocol}//${window.location.hostname}:${window.location.port}`)
}