using OpenQA.Selenium;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestProject1.Pages
{
    public class LoginPage
    {
        public readonly IWebDriver _driver;

        public LoginPage(IWebDriver driver)
        {
            _driver = driver;
        }

        public IWebElement UserNameInput => _driver.FindElement(By.Name("username"));
        public IWebElement PasswordInput => _driver.FindElement(By.Name("password"));
        public IWebElement LoginButton => _driver.FindElement(By.XPath("//*[@id=\"loginForm\"]/div/div[3]/button"));
      
    }
}
