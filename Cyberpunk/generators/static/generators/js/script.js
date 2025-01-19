document.getElementById('networkForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const difficulty = document.getElementById('difficulty').value;
    const branching = document.getElementById('branching').checked;

    try {
        const response = await fetch('', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ difficulty: difficulty, branching: branching })
        });

        if (!response.ok) {
            throw new Error('Ошибка при генерации сети: ' + response.statusText);
        }

        const result = await response.json();
        document.getElementById('result').textContent = JSON.stringify(result, null, 2);
    } catch (error) {
        document.getElementById('result').textContent = 'Ошибка: ' + error.message;
    }
});