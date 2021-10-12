import asyncio
import asynctest
from asynctest import patch
from torpedo.exceptions import BadRequestException
from torpedo.wrappers.db_wrapper import ORMWrapper
from ..managers.user import UserManager
from ..caches import UserCache
from ..managers.question import QuestionManager


class QuestionManagerTest(asynctest.TestCase):
    async def setUp(self):
        self.my_loop = asyncio.new_event_loop()
        self.addCleanup(self.my_loop.close)

    async def tearDown(self):
        self.my_loop.close()

    # @patch.object(UserCache, "get", return_value=[])
    @patch.object(ORMWrapper, "get_by_filters", return_value=[])
    async def test_get_question_raises_exception_with_no_results(
        self, orm_mock, cache_mock
    ):
        # patch.object will set the value of ORMWrapper's get_by_filters method to an empty dict. In UserManager,
        # if an empty queryset is returned then a BadRequestException is raised. So in this test case we are mocking
        # the functionality of the db call without actually making a database call
        await self.assertAsyncRaises(BadRequestException, QuestionManager.get_questions({}))

    @patch.object(UserCache, "set_user", return_value=[])
    @patch.object(UserCache, "get", return_value=[])
    @patch.object(ORMWrapper, "get_by_filters")
    async def test_get_question_with_results_return_success(
        self, orm_mock, cache_mock, cache_set_mock
    ):
        # In this test case we want to validate if a result is returned from the db call then a success is returned
        # from the method without raising an exception. Here we have mocked patched the return value from the database
        # with a mock object which itself is instance of Mock object. The to_dict() method is also mocked with a
        # custom result.
        mock = asynctest.Mock()
        mock.to_dict = asynctest.CoroutineMock(return_value={"question_text": "is sanic good?"})
        orm_mock.return_value = [mock]
        result = await QuestionManager.get_questions({})
        self.assertDictEqual(result, {"question_text": "is sanic good?"})
