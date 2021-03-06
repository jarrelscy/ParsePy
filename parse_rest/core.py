#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


class ParseError(Exception):
    '''Base exceptions from requests made to Parse'''
    pass

class ParseBatchError(Exception):
    ''' Error in batching operation... should take a list. '''
    pass

class ResourceRequestBadRequest(ParseError):
    '''Request returns a 400'''
    pass


class ResourceRequestLoginRequired(ParseError):
    '''Request returns a 401'''
    pass


class ResourceRequestForbidden(ParseError):
    '''Request returns a 403'''
    pass


class ResourceRequestNotFound(ParseError):
    '''Request returns a 404'''
    pass
