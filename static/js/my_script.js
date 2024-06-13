document.addEventListener("DOMContentLoaded", function() {
    if (window.location.pathname.includes("detail")) {
        fetchBrandList();
    }

    const addBrandBtn = document.getElementById("addBrandBtn");
    const sendBrandsBtn = document.getElementById("sendBrandsBtn");
    const brandsContainer = document.getElementById("brandsContainer");

    let brandNames = [];

    function fetchBrandList() {
        fetch('/report/api/brands/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            brandNames = data;
        })
        .catch(error => {
            console.error('Ошибка при получении списка товаров:', error);
        });
    }

    // Function to add brand options
    function addBrandOptions() {
        // Создаем новый выпадающий список
        const rowDiv = document.createElement('div');
        rowDiv.className = 'row';

        // Создаем контейнер для выпадающего списка
        const selectDiv = document.createElement('div');
        selectDiv.className = 'col-sm-6 mt-2';

        // Создаем контейнер для поля ввода
        const inputDiv = document.createElement('div');
        inputDiv.className = 'col-sm-6 mt-2';

        // Создаем новый выпадающий список
        const select = document.createElement("select");
        select.classList.add("form-select");
        brandNames.forEach(brand => {
            const option = document.createElement("option");
            option.value = brand.id;
            option.innerText = brand.name;
            select.appendChild(option);
        });

        // Создаем поле ввода для процентной ставки
        const input = document.createElement("input");
        input.type = "number";
        input.min = 1
        input.placeholder = "Процентная ставка";
        input.classList.add("form-control");

        // Добавляем выпадающий список и поле ввода в их контейнеры
        selectDiv.appendChild(select);
        inputDiv.appendChild(input);

        // Добавляем контейнеры колонок в контейнер строки
        rowDiv.appendChild(selectDiv);
        rowDiv.appendChild(inputDiv);

        // Добавляем контейнер строки в контейнер продуктов
        brandsContainer.appendChild(rowDiv);

        // Для верного отображения следующего ряда добавляем clearfix
        const clearfixDiv = document.createElement('div');
        clearfixDiv.className = 'clearfix';
        brandsContainer.appendChild(clearfixDiv);
    }

    // Функция для сбора и отправки данных
    function sendBrandsData() {
        const allSelects = brandsContainer.querySelectorAll("select");
        const allInputs = brandsContainer.querySelectorAll("input");

        const brandsData = [];

        allSelects.forEach((select, index) => {
            const brandId = select.value;
            const percentageRate = allInputs[index].value;
            brandsData.push({brandId: brandId, rate: percentageRate});
        });

        fetch(window.location.href, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(brandsData),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка сети или сервера');
            }
            return response.json();
        })
        .then(data => {
            if (data.status == 'success') {
                console.log('Успех:', data);
                alert('Данные успешно отправлены!');
                window.location.href = '/';
            } else if (data.status == 'error') {
                alert(data.message);
            }

        })
        .catch(error => {
            console.error('Ошибка:', error);
            alert('Ошибка при отправке данных: ' + error.message);
        });
    }

    addBrandBtn.addEventListener("click", function() {
        addBrandOptions();
    });

    sendBrandsBtn.addEventListener("click", function() {
        sendBrandsData();
    });
});
