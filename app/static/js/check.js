const elem_inps = document.getElementsByClassName('inp');
const elem_alrs = document.getElementsByClassName('alr');
const elem_reqs = document.getElementsByClassName('req');
const alr_data = Object.values(data[1]);
const req_data = Object.values(data[0]);

function calcAlrNum(alr_data) {
	let cnt = 0;
	for (let i = 0; i < alr_data.length; i++) {
		cnt += parseInt(alr_data[i][1]);
	}
	return cnt;
}

function setAlrList(n, alr_data) {
	let set_data = '';
	set_data += '<h3>' + data[0][n][0] + '</h3>';
	for (let i = 0; i < alr_data.length; i++) {
		set_data += alr_data[i][0] + '：' + alr_data[i][1] + '単位<br>'
	}
	sessionStorage.setItem(n, set_data);
}

function showNameList(n) {
	const list = document.getElementById('name_list');
	list.innerHTML = sessionStorage.getItem(n)
}

function addExtra(name, from, to, n) {
	let cnt = 0;
	for (let i = from; i <= to; i++) {
		cnt += calcAlrNum(alr_data[i]);
	}
	const elem_alr = document.getElementsByClassName('alr_' + name)[0];
	const elem_req = document.getElementsByClassName('req_' + name)[0];
	const elem_inp = document.getElementsByClassName('inp_' + name)[0];
	elem_alr.innerHTML = cnt;
	elem_req.innerHTML = n;
	if (cnt < n) {
		elem_inp.setAttribute('style','background-color: salmon;');
	}
	return cnt;
}


for (let i = 0; i < elem_reqs.length; i++) {
	const alr_num = calcAlrNum(alr_data[i]);
	const req_num = req_data[i][1];
	elem_alrs[i].innerHTML = alr_num;
	elem_reqs[i].innerHTML = req_num;
	setAlrList(i, alr_data[i]);
	if (alr_num < req_num && !elem_inps[i].classList.contains('dis_inp')) {
		elem_inps[i].setAttribute('style','background-color: salmon;');
	}
}

addExtra('syudai', 0, 4, 8);
addExtra('gakumon', 7, 8, 8);
addExtra('zen', 0, 11, 26);
addExtra('zengaku', 0, 12, 32);
addExtra('kyotu', 13, 16, 14);
addExtra('senmon', 17, 19, 68);
const gakubu = addExtra('gakubu', 13, 21, 96);
addExtra('goukei', 0, 21, 128);

const elem_alr_jiyuu = document.getElementsByClassName('alr_jiyuu')[0];
const elem_req_jiyuu = document.getElementsByClassName('req_jiyuu')[0];
const elem_inp_jiyuu = document.getElementsByClassName('inp_jiyuu')[0];
const jiyuu = gakubu - 86;
elem_alr_jiyuu.innerHTML = (jiyuu < 0 ? 0 : jiyuu) + '(卒研を取った場合：' + ((jiyuu + 8) < 0 ? 0 : jiyuu + 8) + ')';
elem_req_jiyuu.innerHTML = 6;
if (jiyuu < 6) {
	elem_inp_jiyuu.setAttribute('style','background-color: salmon;');
} else if (jiyuu + 8 < 6) {
	elem_inp_jiyuu.setAttribute('style','background-color: salmon;');
}