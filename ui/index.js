const FUNCTION_URL = "https://europe-west3-regal-campaign-308311.cloudfunctions.net/image-handler"

function setPercents(id, score) {
    let percent = (100 * score).toFixed(2)
    $(`#${id}`).attr('value', percent.toString());
    $(`#${id}-percent`).text(`${percent}%`)
}

function readURL(input) {
    if (input.files && input.files[0]) {
        let reader = new FileReader();

        reader.onload = function (e) {
            $('#uploaded-image')
                .attr('src', e.target.result);
        };

        setPercents('dog', 0)
        setPercents('cat', 0)

        reader.readAsDataURL(input.files[0]);


        let photo = input.files[0]
        let formData = new FormData();
        formData.append("file", photo);
        fetch(FUNCTION_URL, {method: "POST", body: formData}).then(r => {
            r.json().then(response => {
                console.log(response)
                let dog = response.find(o => o.label === "Dog")
                let cat = response.find(o => o.label === "Cat")

                if (dog !== undefined) {
                    setPercents('dog', dog.score)
                }
                if (cat !== undefined) {
                    setPercents('cat', cat.score)
                }
            })
        });

    }
}
