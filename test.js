var input = [
    {in : 1, out: 4},
    {in : 2, out: 5},
    {in : 10, out: 12},
    {in : 5, out: 9},
    {in : 5, out: 12}
];

const types = {
    in: 1,
    out: 0,
}

function maxGuests(arr) {
    if(!arr || arr.length === 0) {
        return 0;
    }
    var totalDays = [];
    var data = {
        max: 0,
        day: undefined,
        count: 0,
    };
    for(var i = 0; i < arr.length; i++){
        var curr = arr[i];
        totalDays.push({key: curr.in, type: types.in });
        totalDays.push({key: curr.out, type: types.out });
    }
    totalDays.sort((a, b) => {
        var temp = a.key - b.key;
        if(temp === 0) {
            return b.type - a.type;
        }
        return temp;
    });

    for (let i = 0; i < totalDays.length; i++) {
        var temp = totalDays[i];
        switch(temp.type) {
            case 1: {
                data.count++;
                if(data.max < data.count) {
                    data.max = data.count;
                    data.day = temp.key;
                }
                break;
            }
            case 0: {
                data.count--;
                break;
            }
            default:
                break;
        }
    }

    return data.day;
}

var day = maxGuests(input);
console.log('max guests on day ', day);
