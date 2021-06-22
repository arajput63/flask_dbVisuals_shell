var output = document.getElementById("test_output");

async function test_clicked() {
    const res = await fetch('/_test_query', {method: "GET",}); // create a fetch request to the server
    const update = await res.json(); // store the response in a constant
    if (res.ok && res.status == 200){
        console.log(update); // log the response to browser console
        output.innerText = update.test_results; //update the text to show the results
    } else { 
        console.log("Error retrieving test row from database...") 
    }
}