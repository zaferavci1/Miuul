const rl = require('readline-sync');
const colors = require('colors');
const title = require('./modules/title.js');
const fastBomber = require('./modules/sms.js');

title('Hosgeldiniz');

let telefon = rl.question(' West Sms Bomber;Telefon Numarasi Giriniz : ' .blue);
if (telefon.length != 10) {
    console.log('Telefon Numarasi 10 Haneli Olmalidir. Ex: 5401234521'.blue);
    process.exit(1);
}
title('Numara: ' + telefon);

let miktar = rl.question("Kac Adet SMS Gondermek Istiyorsunuz: ".white);
if(isNaN(miktar)) return console.log('Lutfen Bir Rakam Giriniz'.blue) && process.exit(1);
if (miktar.length == 0) {
    console.log('Miktar Giriniz'.blue);
    process.exit(1);
}
title(`Telefon: ${telefon} - Miktar: ${miktar}`);

console.log('SMS Gonderiliyor...'.blue);

fastBomber(telefon, miktar);
