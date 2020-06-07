$("#input-form").submit(function (e) {
  e.preventDefault()

  var form = $(this)
  var url = form.attr('action')
  const tableDOM = document.querySelector(".our-table")
  $.ajax({
    type: "POST",
    url: '/fuzzyWuzzyScorers',
    data: form.serialize(),
    success: function (data) {
      data = JSON.parse(data);
      let result = ''
      data.forEach((score) => {
        result += `
         <tr class ="success"> <td><b>${score.scorer_name}</b></td> <td><b>${score.similarity_score}</b></td></tr>`
      })
      tableDOM.innerHTML = result

    },
    error: function (error) {
      console.log("inside error")
      console.log(e)
    }

  })


})
