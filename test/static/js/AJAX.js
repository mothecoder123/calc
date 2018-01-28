//ajax
function sendKey(key)
{
//    alert(key)
    var req = new XMLHttpRequest()
    req.onreadystatechange = function()
    {
        if (req.readyState == 4)
        {
            if (req.status != 200)
            {
                //error handling code here
            }
            else
            {
                var response = JSON.parse(req.responseText)
                document.getElementById('display').innerHTML = response.display
                document.getElementById('currentAction').innerHTML = response.action
            }
        }
    }
    req.open('POST', '/')
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")

    var currentDisplay = document.getElementById('display').innerHTML;
    var currentAction = document.getElementById('currentAction').innerHTML;

//    alert(currentAction)

    var postVars = 'function=sendKey&key='+key+'&currentDisplay='+currentDisplay+'&currentAction='+currentAction
    req.send(postVars)
//    alert(postVars)
    return false
}

