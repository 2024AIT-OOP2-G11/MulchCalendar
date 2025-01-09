//const ics = require('ics') 
//import * as ics from '..' 
//const { writeFileSync } = require('fs')

//debug用
const event = [['demo','This is thirty minute event', 'Nome, AK', '8/7/2024 5:30 pm', '8/7/2024 6:00 pm'],
                ['test', 'This is an all day event', 'Nome, AK', '9/1/2024', '9/1/2024']];

//icsイベントを作成
document.getElementById('download-btn').addEventListener('click', () => {
  var cal =ics();
	//cal.addEvent('Demo Event', 'This is thirty minute event', 'Nome, AK', '8/7/2013 5:30 pm', '8/7/2013 6:00 pm');
  for (let i = 0;i < 2;i++)
    cal.addEvent(event[i][0],event[i][1],event[i][2],event[i][3],event[i][4]);
  cal.download("Event");
});
console.log(ics);