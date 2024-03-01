const problems = [
    {
        id: "ti_geometpdf_01a",
        answers: [
            0.018
        ]
    }
];

function handleInput(event) {
    console.log(event);

    if(event.key == "Enter") {
        event.preventDefault();
        var corretAnswers = problems.filter( problem => problem.id === event.target.id).pop().answers
        var userAnswer = document.getElementById(event.target.id).value
        if (corretAnswers.includes(userAnswer)) {
            console.log("happy fun time");
        }
        else {
            console.log("awful bad time")
        }
    }

}

problems.forEach( problem => {
    var input = document.getElementById(problem.id);
    if(input) input.addEventListener("keypress", handleInput)
});