
/*

1. Abrir un csv

2. Hacer request GET

3. Grabar headers

4. Grabar datos 

5. 

*/

///////////////////////////////////////////////////////////////////////////////////////

const superagent = require('superagent');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

const url = 'https://catfact.ninja/fact'; 

superagent.get(url).end((err, res) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = [res.body];
  const headers = Object.keys(data[0]);
  console.log(data)
  
  const csvWriter = createCsvWriter({
    path: 'catfacts.csv',
    header: headers.map((header) => {
      return { id: header, title: header };
    })
  });
  
  csvWriter.writeRecords(data)
    .then(() => {
      console.log('CSV file has been written');
    });
});

  
