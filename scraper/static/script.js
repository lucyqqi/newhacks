
// import data from 'http://127.0.0.1:5500/scraper/output.jsonl' assert {type: 'json'}
fetch("http://127.0.0.1:5500/scraper/output.json")
  .then(response => response.json())
  .then(json => {

    document.getElementById("name1").innerText = json.product1.name;
    document.getElementById("name2").innerText = json.product2.name;
    document.getElementById("price1").innerText = json.product1.price;
    document.getElementById("price2").innerText = json.product2.price;
    document.getElementById("rating1").innerText = json.product1.review_count;
    document.getElementById("rating2").innerText = json.product2.review_count;

  }
  );
