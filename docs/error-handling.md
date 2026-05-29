# Error Handling

Unhandled exceptions are converted to a JSON `500` response by
`add_exception_handlers`.

The handler logs the path and exception stack but only returns the exception
class name and a generic detail message to the client.
