document.addEventListener("DOMContentLoaded", function() {
    if (window.location.pathname.includes("detail")) {
        fetchBrandList(); // Загрузка данных продуктов сразу при загрузке страницы
    }

    const addBrandBtn = document.getElementById("addBrandBtn");
    const brandsContainer = document.getElementById("brandsContainer");

    let brandNames = []; // Здесь будем хранить список продуктов

    function fetchBrandList() {
        fetch('/report/api/brands/', {
            method: 'GET', // или 'POST', если ваш API требует другой метод
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            brandNames = data; // Сохраняем полученные данные о продуктах
        })
        .catch(error => {
            console.error('Ошибка при получении списка товаров:', error);
        });
    }

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

    addBrandBtn.addEventListener("click", function() {
        addBrandOptions(); // Добавление выпадающего списка при клике на кнопку
    });
});
