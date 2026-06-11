import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.step("Перетаскивание элемента")
def drag_and_drop(driver, source_locator, target_locator, timeout=10):
    source = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(source_locator)
    )
    target = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(target_locator)
    )
    
    # Прокрутка к элементам
    driver.execute_script("arguments[0].scrollIntoView(true);", source)
    driver.execute_script("arguments[0].scrollIntoView(true);", target)
    
    # Универсальный JavaScript для перетаскивания (работает и в Chrome, и в Firefox)
    driver.execute_script("""
        function createEvent(type, target) {
            var event = new DragEvent(type, {
                bubbles: true,
                cancelable: true,
                dataTransfer: new DataTransfer()
            });
            target.dispatchEvent(event);
            return event;
        }
        
        var source = arguments[0];
        var target = arguments[1];
        
        // Начало перетаскивания
        var dragStartEvent = createEvent('dragstart', source);
        
        // Перетаскивание
        var dragEvent = createEvent('drag', source);
        
        // Завершение перетаскивания над целью
        var dragEnterEvent = createEvent('dragenter', target);
        var dragOverEvent = createEvent('dragover', target);
        var dropEvent = createEvent('drop', target);
        
        // Завершение перетаскивания
        var dragEndEvent = createEvent('dragend', source);
    """, source, target)
    
    # Небольшая задержка для завершения анимации
    driver.implicitly_wait(1)