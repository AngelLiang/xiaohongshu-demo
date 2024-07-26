document.getElementById("generate").onclick = function () {
    const input = document.getElementById("input").value;
    if (!input) {
        return alert('请输入内容');
    }
    cleanOutput()
    fetchData(input, (data) => {
        // 回调时执行以下代码
        document.getElementById('output').innerHTML += data;
    });
}

const fetchData = async function (input, callback) {
    const response = await fetch('/api/generate', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt: input })
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
