var output = document.getElementById("test_output");

async function test_clicked() {
    const res = await fetch('/_test_query', {method: "GET",});
    const update = await res.json();
    if (res.ok && res.status == 200){
        console.log(update);
        output.innerText = update.test_results;
    } else { 
        console.log("Error retrieving test row from database...") 
    }
}