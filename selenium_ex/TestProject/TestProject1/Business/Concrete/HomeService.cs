using OpenQA.Selenium;
using OpenQA.Selenium.Support.UI;
using SeleniumExtras.WaitHelpers;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using TestProject1.Business.Abstract;
using TestProject1.Pages;

namespace TestProject1.Business.Concrete
{
    public class HomeService : IHomeService
    {
        public readonly IWebDriver _driver;
        public readonly HomePage _homepage;

        public HomeService(IWebDriver driver)
        {
            _driver = driver;
            _homepage = new HomePage(_driver);
        }



        public void GoProfile()
        {
            WebDriverWait wait = new WebDriverWait(_driver, TimeSpan.FromSeconds(10));
            wait.Until(ExpectedConditions.ElementIsVisible(By.XPath("//span[text()='Profil']")));
            if(_homepage.ProfileButton.Displayed)
            {
                _homepage.ProfileButton.Click();
                Thread.Sleep(7000);
            }

        }
    }
}
