
id = 0;

function addQuestion(type)
{
    if(type === 'text')
    {
        id++;
        addText();
    }
    else if(type === 'radio')
    {
        id++;
    }
    else if(type === 'checkbox')
    {
        id++;
    }
}

function addText()
{
    textToAdd = "<tr>";
    textToAdd += addQuestionText();
    textToAdd += addInput();
    textToAdd += addRemoveBtn();
    textToAdd += "</tr>";
    $('table').append( textToAdd );

}

function addQuestionText()
{
    return "<td><lable id='qtext" + id.toString() + "'> question " + id.toString() + " </lable> </td>"
}

function addInput()
{
    return "<td><input type='text' name='q" + id.toString() + "' id='q" + id.toString() + "'> </td>"

}

function addRemoveBtn()
{
    return "<td><input type='button' class='btn' onclick='remove(" + id.toString() + ")' style='background:red' value='x' name='remq" + id.toString() + "' id='remq" + id.toString() + "'> </td>"
}

function remove(remid)
{
    if(remid == id)
    {
        id--;
    }
    else{
        for(var i = remid + 1; i <= id; i++)
        {
            document.getElementById("q" + i.toString()).id = "q" + (i - 1).toString();
            document.getElementById("qtext" + i.toString()).innerHtml = "question" + (i - 1).toString();
            document.getElementById("qtext" + i.toString()).id = "qtext" + (i - 1).toString();
            document.getElementById("remq" + i.toString()).onclick = 'remove(' + (i - 1).toString() + ')';
        }
    }
    document.getElementById("questions").deleteRow(remid - 1);
    id--;
}

















