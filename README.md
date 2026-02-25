# RECRUITMENT-APPLICATION-TRACKER
let d=document,l=JSON.parse(localStorage.rat||'[]'),r=()=>{ d.body.innerHTML='&lt;form onsubmit="l.push({c:q.value,s:s.value});localStorage.rat=JSON.stringify(l)">'+ '&lt;input id=q>&lt;select id=s>&lt;option>Applied&lt;option>Interview&lt;/select>&lt;button>Add&lt;/button>&lt;/form>'+ l.map(a=>`&lt;div>${a.c} - ${a.s}&lt;/div>`).join('')};r()
