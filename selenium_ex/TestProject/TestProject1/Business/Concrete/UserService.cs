using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;
using SeleniumExtras.WaitHelpers;
using System;
using TestProject1.Pages.Abstract;

namespace TestProject1.Pages.Concrete
{
    public class UserService : IUserService
    {
        public readonly IWebDriver _driver;
        public readonly LoginPage _loginPage;
        public readonly HomePage _homepage;

        public UserService(IWebDriver driver)
        {
            _driver = driver;
            _loginPage = new LoginPage(_driver);
            _homepage = new HomePage(_driver);
        }

        public void TrueLogin(string username, string password)
        {
            _driver.Navigate().GoToUrl("https://www.instagram.com/");
            _driver.Manage().Window.Maximize();


            WebDriverWait wait = new WebDriverWait(_driver, TimeSpan.FromSeconds(10));
            wait.Until(d => ((IJavaScriptExecutor)d).ExecuteScript("return document.readyState").Equals("complete"));

            _loginPage.UserNameInput.SendKeys(username);
            _loginPage.PasswordInput.SendKeys(password);
            _loginPage.LoginButton.Click();
            wait.Until(ExpectedConditions.ElementIsVisible(By.XPath("//div[@role=\"button\" and text() =\"Şimdi değil\"]")));
            Thread.Sleep(2000);

            _homepage.SDegil1.Click();
            Thread.Sleep(2000);
            _homepage.ClickSecondButtonInsideButton2();
            Thread.Sleep(2000);

        }

        public void Logout()
        {
            WebDriverWait wait = new WebDriverWait(_driver, TimeSpan.FromSeconds(10));
            wait.Until(ExpectedConditions.ElementIsVisible(By.XPath("//span[text()='Daha fazla']")));
            if (_homepage.DahaFazla.Displayed)
            {
                _homepage.DahaFazla.Click();
                wait.Until(ExpectedConditions.ElementIsVisible(By.XPath("//span[text()='Çıkış yap']")));
                _homepage.Logout.Click();
                Thread.Sleep(7000);
            }

        }
    }
}
