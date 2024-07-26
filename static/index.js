document.getElementById("generate").onclick = function () {
    const input = document.getElementById("input").value;
    const isStream = document.getElementById("isStream").checked;  // 获取复选框的状态

    if (!input) {
        return alert('请输入内容');
    }

    cleanOutput();

    fetchData(input, isStream, (data) => {  // 将复选框的状态作为参数传给fetchData函数
        // 回调时执行以下代码
        document.getElementById('output').innerHTML += data;
    });
}


const fetchData = async function (input, isStream, callback) {
    const response = await fetch('/api/generate', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt: input, stream: isStream })
    })

    const reader = response.body.getReader();
    // 获取实时返回的数据
    while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const data = new TextDecoder().decode(value);
        // 这是一个回调函数
        callback(data)
    }
};


const cleanOutput = function () {
    document.getElementById('output').innerHTML = ''
}
