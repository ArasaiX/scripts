const prompt = require('prompt-sync')({sigint: true});
const superagent = require('superagent');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

/* 
    Before run this script choose if want to prompt the data first or hardcode
*/

// const vtexApiKey = prompt('Enter the api Key: ');
// const vtexApiToken = prompt('Enter the api Token: ');
// const accountName = prompt('Enter the account name: ');
// const environment = prompt('Enter the environment: ');
// let url = prompt('Enter the url(without the "https://" and account name/environment)\nFor example (/api/dataentities/{dataEntityName}/scroll)');
// let secondUrl = prompt('Enter the second url if your call have more one pages (same format of the last one):')
// let filename = prompt('Enter the output filename:');
// filename = filename + '.csv';

// const vtexApiKey = '';
// const vtexApiToken = '';
// const accountName = '';
// const environment = '';
// let url = '';
// let secondUrl = '';
// let filename = 'output.csv'


url = `https://${accountName}.${environment}.com.br${url}`;

const headersRequest = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-VTEX-API-AppKey": vtexApiKey,
    "X-VTEX-API-AppToken": vtexApiToken
}

superagent
        .get(url)
        .set(headersRequest)
        .end((err, res) => {
    if (err) {
        console.log(err);
        return;
    }
    
    const jsonData = res

    console.log(jsonData)

    token = res.headers['x-vtex-md-token'];

    const keyHeaders = Object.keys(jsonData)

    console.log(keyHeaders)

    const csvWriter = createCsvWriter ({
        path:`./${filename}.csv`,
        header: [
            keyHeaders.forEach(element, index => id = element[index], title = element[index])
        ]
    })

    csvWriter.writeRecords(response)
        .then(() => {
            console.log('First page writen... I keep writing...');
        });
    
        cacheTimeControl = res.headers['x-vtex-cache-time']

    let condition = true
  
    while (condition) {
    secondUrl = `https://${accountName}.${environment}.com.br${secondUrl}${token}`;
    superagent
        .get(url)
        .set(headersRequest)
        .end((error, response) => {
        if (error) {
            console.log(error);
        return;
    }
    try {
        cacheTimeControl = response.headers['x-vtex-cache-time']
        csvWriter.writeRecords(response)
            .then(() => {
            console.log('CSV file has been written');
    });
    } catch (Exception){
        console.log(Exception)
        
    }finally {
        return;
    }
    });

    }

});
