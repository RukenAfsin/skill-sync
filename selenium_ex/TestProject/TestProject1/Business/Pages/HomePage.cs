using OpenQA.Selenium;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestProject1.Pages
{
    public class HomePage
    {
        public readonly IWebDriver _driver;

        public HomePage(IWebDriver driver)
        {
            _driver = driver;
        }
        public IWebElement SDegil1 => _driver.FindElement(By.XPath("//div[@role=\"button\" and text() =\"Şimdi değil\"]"));
        public IWebElement SDegil2 => _driver.FindElement(By.ClassName("_a9-z"));
        public IWebElement DahaFazla => _driver.FindElement(By.XPath("//span[text()='Daha fazla']"));
        public IWebElement Logout => _driver.FindElement(By.XPath("//span[text()='Çıkış yap']"));
        public IWebElement ProfileButton => _driver.FindElement(By.XPath( "//span[text()='Profil']"));



        public void ClickSecondButtonInsideButton2()
        {
            var buttons = SDegil2.FindElements(By.TagName("button"));
            if (buttons.Count > 1)
            {
                buttons[1].Click();
            }
            else
            {
                throw new NoSuchElementException("Second button inside Button2 not found.");
            }
        }
    }
}
