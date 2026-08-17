async function loadTasks() {
    const res = await fetch("/tasks");
    const tasks = await res.json();
    const list = document.getElementById("taskList");
    list.innerHTML = "";
    tasks.forEach(task => {
        const li = document.createElement("li");
        li.textContent = task.title + (task.done ? " (done)" : "");
        list.appendChild(li);
    });
}

async function addTask() {
    const input = document.getElementById("taskInput");
    const title = input.value;
    if (!title) return;

    await fetch("/tasks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title: title })
    });

    input.value = "";
    loadTasks();
}

loadTasks();