/* Generated code for Python source for module '__main__'
 * created by Nuitka version 0.5.27
 *
 * This code is in part copyright 2017 Kay Hayen.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "nuitka/prelude.h"

#include "__helpers.h"

/* The _module___main__ is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module___main__;
PyDictObject *moduledict___main__;

/* The module constants used, if any. */
static PyObject *const_str_plain___package__;
static PyObject *const_str_plain_sys;
static PyObject *const_str_digest_06d1d820ac431f43bda79bb4fff3f770;
extern PyObject *const_str_plain___file__;
static PyObject *const_str_digest_ae0b57ade6d4164d9a0447273a969336;
extern PyObject *const_int_0;
static PyObject *const_str_digest_5d01e8dbd25ef675458e69951213f0e9;
extern PyObject *const_str_plain_print;
extern PyObject *const_str_plain_site;
extern PyObject *const_str_plain_types;
static PyObject *const_str_digest_b7ce623762227beef9ef9f0c96dc984c;
static PyObject *const_tuple_str_digest_ae0b57ade6d4164d9a0447273a969336_tuple;
static PyObject *const_str_plain_os;
static PyObject *const_str_angle_module;
extern PyObject *const_tuple_empty;
static PyObject *const_tuple_str_digest_5d01e8dbd25ef675458e69951213f0e9_tuple;
extern PyObject *const_str_plain___main__;
static PyObject *const_str_plain_read;
static PyObject *const_str_angle_string;
static PyObject *const_str_plain___annotations__;
static PyObject *const_str_digest_1b3f248c1673fa0c4f4c9b81d2e9c606;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_str_plain___cached__;
static PyObject *const_str_plain_exec;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_str_plain___package__ = UNSTREAM_STRING( &constant_bin[ 0 ], 11, 1 );
    const_str_plain_sys = UNSTREAM_STRING( &constant_bin[ 11 ], 3, 1 );
    const_str_digest_06d1d820ac431f43bda79bb4fff3f770 = UNSTREAM_STRING( &constant_bin[ 14 ], 15, 0 );
    const_str_digest_ae0b57ade6d4164d9a0447273a969336 = UNSTREAM_STRING( &constant_bin[ 29 ], 28, 0 );
    const_str_digest_5d01e8dbd25ef675458e69951213f0e9 = UNSTREAM_STRING( &constant_bin[ 57 ], 14, 0 );
    const_str_digest_b7ce623762227beef9ef9f0c96dc984c = UNSTREAM_STRING( &constant_bin[ 71 ], 19, 0 );
    const_tuple_str_digest_ae0b57ade6d4164d9a0447273a969336_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_digest_ae0b57ade6d4164d9a0447273a969336_tuple, 0, const_str_digest_ae0b57ade6d4164d9a0447273a969336 ); Py_INCREF( const_str_digest_ae0b57ade6d4164d9a0447273a969336 );
    const_str_plain_os = UNSTREAM_STRING( &constant_bin[ 90 ], 2, 1 );
    const_str_angle_module = UNSTREAM_STRING( &constant_bin[ 92 ], 8, 0 );
    const_tuple_str_digest_5d01e8dbd25ef675458e69951213f0e9_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_digest_5d01e8dbd25ef675458e69951213f0e9_tuple, 0, const_str_digest_5d01e8dbd25ef675458e69951213f0e9 ); Py_INCREF( const_str_digest_5d01e8dbd25ef675458e69951213f0e9 );
    const_str_plain_read = UNSTREAM_STRING( &constant_bin[ 100 ], 4, 1 );
    const_str_angle_string = UNSTREAM_STRING( &constant_bin[ 104 ], 8, 0 );
    const_str_plain___annotations__ = UNSTREAM_STRING( &constant_bin[ 112 ], 15, 1 );
    const_str_digest_1b3f248c1673fa0c4f4c9b81d2e9c606 = UNSTREAM_STRING( &constant_bin[ 127 ], 60, 0 );
    const_str_plain_exec = UNSTREAM_STRING( &constant_bin[ 187 ], 4, 1 );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants___main__( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_f339eee560542cbb53639d46377c272c;
/* For use in "MainProgram.c". */
PyCodeObject *codeobj_main = NULL;

static void createModuleCodeObjects(void)
{
    module_filename_obj = const_str_digest_1b3f248c1673fa0c4f4c9b81d2e9c606;
    codeobj_f339eee560542cbb53639d46377c272c = MAKE_CODEOBJ( module_filename_obj, const_str_angle_module, 1, const_tuple_empty, 0, 0, CO_NOFREE );
    codeobj_main = codeobj_f339eee560542cbb53639d46377c272c;
}

// The module function declarations.


// The module function definitions.



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef___main__ =
{
    PyModuleDef_HEAD_INIT,
    "__main__",   /* m_name */
    NULL,                /* m_doc */
    -1,                  /* m_size */
    NULL,                /* m_methods */
    NULL,                /* m_reload */
    NULL,                /* m_traverse */
    NULL,                /* m_clear */
    NULL,                /* m_free */
  };
#endif

#if PYTHON_VERSION >= 300
extern PyObject *metapath_based_loader;
#endif
#if PYTHON_VERSION >= 330
extern PyObject *const_str_plain___loader__;
#endif

extern void _initCompiledCellType();
extern void _initCompiledGeneratorType();
extern void _initCompiledFunctionType();
extern void _initCompiledMethodType();
extern void _initCompiledFrameType();
#if PYTHON_VERSION >= 350
extern void _initCompiledCoroutineTypes();
#endif
#if PYTHON_VERSION >= 360
extern void _initCompiledAsyncgenTypes();
#endif

// The exported interface to CPython. On import of the module, this function
// gets called. It has to have an exact function name, in cases it's a shared
// library export. This is hidden behind the MOD_INIT_DECL.

MOD_INIT_DECL( __main__ )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module___main__ );
    }
    else
    {
        _init_done = true;
    }
#endif

#ifdef _NUITKA_MODULE
    // In case of a stand alone extension module, need to call initialization
    // the init here because that's the first and only time we are going to get
    // called here.

    // Initialize the constant values used.
    _initBuiltinModule();
    createGlobalConstants();

    /* Initialize the compiled types of Nuitka. */
    _initCompiledCellType();
    _initCompiledGeneratorType();
    _initCompiledFunctionType();
    _initCompiledMethodType();
    _initCompiledFrameType();
#if PYTHON_VERSION >= 350
    _initCompiledCoroutineTypes();
#endif
#if PYTHON_VERSION >= 360
    _initCompiledAsyncgenTypes();
#endif

#if PYTHON_VERSION < 300
    _initSlotCompare();
#endif
#if PYTHON_VERSION >= 270
    _initSlotIternext();
#endif

    patchBuiltinModule();
    patchTypeComparison();

    // Enable meta path based loader if not already done.
    setupMetaPathBasedLoader();

#if PYTHON_VERSION >= 300
    patchInspectModule();
#endif

#endif

    /* The constants only used by this module are created now. */
#ifdef _NUITKA_TRACE
    puts("__main__: Calling createModuleConstants().");
#endif
    createModuleConstants();

    /* The code objects used by this module are created now. */
#ifdef _NUITKA_TRACE
    puts("__main__: Calling createModuleCodeObjects().");
#endif
    createModuleCodeObjects();

    // puts( "in init__main__" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module___main__ = Py_InitModule4(
        "__main__",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module___main__ = PyModule_Create( &mdef___main__ );
#endif

    moduledict___main__ = (PyDictObject *)((PyModuleObject *)module___main__)->md_dict;

    CHECK_OBJECT( module___main__ );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_plain___main__, module___main__ );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module___main__ );

    if ( PyDict_GetItem( module_dict, const_str_plain___builtins__ ) == NULL )
    {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then.
#if !defined(_NUITKA_EXE) || !1
        value = PyModule_GetDict( value );
#endif

#ifndef __NUITKA_NO_ASSERT__
        int res =
#endif
            PyDict_SetItem( module_dict, const_str_plain___builtins__, value );

        assert( res == 0 );
    }

#if PYTHON_VERSION >= 330
    PyDict_SetItem( module_dict, const_str_plain___loader__, metapath_based_loader );
#endif

    // Temp variables if any
    PyObject *tmp_exec_call_1__globals = NULL;
    PyObject *tmp_exec_call_1__locals = NULL;
    PyObject *tmp_exec_call_2__globals = NULL;
    PyObject *tmp_exec_call_2__locals = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *exception_keeper_type_2;
    PyObject *exception_keeper_value_2;
    PyTracebackObject *exception_keeper_tb_2;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_2;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_assign_source_3;
    PyObject *tmp_assign_source_4;
    PyObject *tmp_assign_source_5;
    PyObject *tmp_assign_source_6;
    PyObject *tmp_assign_source_7;
    PyObject *tmp_assign_source_8;
    PyObject *tmp_assign_source_9;
    PyObject *tmp_called_instance_1;
    PyObject *tmp_called_instance_2;
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_eval_compiled_1;
    PyObject *tmp_eval_compiled_2;
    PyObject *tmp_eval_globals_1;
    PyObject *tmp_eval_globals_2;
    PyObject *tmp_eval_locals_1;
    PyObject *tmp_eval_locals_2;
    PyObject *tmp_eval_source_1;
    PyObject *tmp_eval_source_2;
    PyObject *tmp_level_name_1;
    PyObject *tmp_level_name_2;
    PyObject *tmp_level_name_3;
    PyObject *tmp_level_name_4;
    PyObject *tmp_name_name_1;
    PyObject *tmp_name_name_2;
    PyObject *tmp_name_name_3;
    PyObject *tmp_name_name_4;
    PyObject *tmp_open_filename_1;
    PyObject *tmp_open_filename_2;
    PyObject *tmp_outline_return_value_1;
    PyObject *tmp_outline_return_value_2;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    tmp_outline_return_value_1 = NULL;
    tmp_outline_return_value_2 = NULL;
    struct Nuitka_FrameObject *frame_f339eee560542cbb53639d46377c272c;


    // Module code.
    // Frame without reuse.
    frame_f339eee560542cbb53639d46377c272c = MAKE_MODULE_FRAME( codeobj_f339eee560542cbb53639d46377c272c, module___main__ );

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack( frame_f339eee560542cbb53639d46377c272c );
    assert( Py_REFCNT( frame_f339eee560542cbb53639d46377c272c ) == 2 );

    // Framed code:
    tmp_name_name_1 = const_str_plain_os;
    tmp_level_name_1 = const_int_0;
    frame_f339eee560542cbb53639d46377c272c->m_frame.f_lineno = 1;
    tmp_unused = IMPORT_MODULE_KW( tmp_name_name_1, NULL, NULL, NULL, tmp_level_name_1 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;

        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_name_name_2 = const_str_plain_sys;
    tmp_level_name_2 = const_int_0;
    frame_f339eee560542cbb53639d46377c272c->m_frame.f_lineno = 1;
    tmp_unused = IMPORT_MODULE_KW( tmp_name_name_2, NULL, NULL, NULL, tmp_level_name_2 );
    assert( tmp_unused != NULL );
    Py_DECREF( tmp_unused );
    tmp_name_name_3 = const_str_plain_types;
    tmp_level_name_3 = const_int_0;
    frame_f339eee560542cbb53639d46377c272c->m_frame.f_lineno = 1;
    tmp_unused = IMPORT_MODULE_KW( tmp_name_name_3, NULL, NULL, NULL, tmp_level_name_3 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;

        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_name_name_4 = const_str_plain_site;
    tmp_level_name_4 = const_int_0;
    frame_f339eee560542cbb53639d46377c272c->m_frame.f_lineno = 1;
    tmp_unused = IMPORT_MODULE_KW( tmp_name_name_4, NULL, NULL, NULL, tmp_level_name_4 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;

        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_assign_source_1 = Py_None;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = const_str_digest_1b3f248c1673fa0c4f4c9b81d2e9c606;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    tmp_assign_source_3 = Py_None;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___cached__, tmp_assign_source_3 );
    tmp_assign_source_4 = Py_None;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___package__, tmp_assign_source_4 );
    tmp_assign_source_5 = PyDict_New();
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain___annotations__, tmp_assign_source_5 );
    tmp_called_name_1 = LOOKUP_BUILTIN( const_str_plain_print );
    assert( tmp_called_name_1 != NULL );
    frame_f339eee560542cbb53639d46377c272c->m_frame.f_lineno = 2;
    tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, &PyTuple_GET_ITEM( const_tuple_str_digest_5d01e8dbd25ef675458e69951213f0e9_tuple, 0 ) );

    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 2;

        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_assign_source_6 = ((PyModuleObject *)module___main__)->md_dict;
    assert( tmp_exec_call_1__locals == NULL );
    Py_INCREF( tmp_assign_source_6 );
    tmp_exec_call_1__locals = tmp_assign_source_6;

    tmp_assign_source_7 = ((PyModuleObject *)module___main__)->md_dict;
    assert( tmp_exec_call_1__globals == NULL );
    Py_INCREF( tmp_assign_source_7 );
    tmp_exec_call_1__globals = tmp_assign_source_7;

    // Tried code:
    tmp_open_filename_1 = const_str_digest_06d1d820ac431f43bda79bb4fff3f770;
    tmp_called_instance_1 = BUILTIN_OPEN( tmp_open_filename_1, NULL, NULL, NULL, NULL, NULL, NULL, NULL );
    if ( tmp_called_instance_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 3;

        goto try_except_handler_1;
    }
    frame_f339eee560542cbb53639d46377c272c->m_frame.f_lineno = 3;
    tmp_eval_source_1 = CALL_METHOD_NO_ARGS( tmp_called_instance_1, const_str_plain_read );
    Py_DECREF( tmp_called_instance_1 );
    if ( tmp_eval_source_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 3;

        goto try_except_handler_1;
    }
    tmp_eval_globals_1 = tmp_exec_call_1__globals;

    CHECK_OBJECT( tmp_eval_globals_1 );
    tmp_eval_locals_1 = tmp_exec_call_1__locals;

    CHECK_OBJECT( tmp_eval_locals_1 );
    tmp_eval_compiled_1 = COMPILE_CODE( tmp_eval_source_1, const_str_angle_string, const_str_plain_exec, NULL, NULL, NULL );
    Py_DECREF( tmp_eval_source_1 );
    if ( tmp_eval_compiled_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 3;

        goto try_except_handler_1;
    }
    tmp_outline_return_value_1 = EVAL_CODE( tmp_eval_compiled_1, tmp_eval_globals_1, tmp_eval_locals_1 );
    Py_DECREF( tmp_eval_compiled_1 );
    if ( tmp_outline_return_value_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 3;

        goto try_except_handler_1;
    }
    goto try_return_handler_1;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( __main__ );
    return MOD_RETURN_VALUE( NULL );
    // Return handler code:
    try_return_handler_1:;
    Py_XDECREF( tmp_exec_call_1__globals );
    tmp_exec_call_1__globals = NULL;

    Py_XDECREF( tmp_exec_call_1__locals );
    tmp_exec_call_1__locals = NULL;

    goto outline_result_1;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF( tmp_exec_call_1__globals );
    tmp_exec_call_1__globals = NULL;

    Py_XDECREF( tmp_exec_call_1__locals );
    tmp_exec_call_1__locals = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto frame_exception_exit_1;
    // End of try:
    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( __main__ );
    return MOD_RETURN_VALUE( NULL );
    outline_result_1:;
    tmp_unused = tmp_outline_return_value_1;
    Py_DECREF( tmp_unused );
    tmp_called_name_2 = LOOKUP_BUILTIN( const_str_plain_print );
    assert( tmp_called_name_2 != NULL );
    frame_f339eee560542cbb53639d46377c272c->m_frame.f_lineno = 5;
    tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_2, &PyTuple_GET_ITEM( const_tuple_str_digest_ae0b57ade6d4164d9a0447273a969336_tuple, 0 ) );

    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 5;

        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_assign_source_8 = ((PyModuleObject *)module___main__)->md_dict;
    assert( tmp_exec_call_2__locals == NULL );
    Py_INCREF( tmp_assign_source_8 );
    tmp_exec_call_2__locals = tmp_assign_source_8;

    tmp_assign_source_9 = ((PyModuleObject *)module___main__)->md_dict;
    assert( tmp_exec_call_2__globals == NULL );
    Py_INCREF( tmp_assign_source_9 );
    tmp_exec_call_2__globals = tmp_assign_source_9;

    // Tried code:
    tmp_open_filename_2 = const_str_digest_b7ce623762227beef9ef9f0c96dc984c;
    tmp_called_instance_2 = BUILTIN_OPEN( tmp_open_filename_2, NULL, NULL, NULL, NULL, NULL, NULL, NULL );
    if ( tmp_called_instance_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 6;

        goto try_except_handler_2;
    }
    frame_f339eee560542cbb53639d46377c272c->m_frame.f_lineno = 6;
    tmp_eval_source_2 = CALL_METHOD_NO_ARGS( tmp_called_instance_2, const_str_plain_read );
    Py_DECREF( tmp_called_instance_2 );
    if ( tmp_eval_source_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 6;

        goto try_except_handler_2;
    }
    tmp_eval_globals_2 = tmp_exec_call_2__globals;

    CHECK_OBJECT( tmp_eval_globals_2 );
    tmp_eval_locals_2 = tmp_exec_call_2__locals;

    CHECK_OBJECT( tmp_eval_locals_2 );
    tmp_eval_compiled_2 = COMPILE_CODE( tmp_eval_source_2, const_str_angle_string, const_str_plain_exec, NULL, NULL, NULL );
    Py_DECREF( tmp_eval_source_2 );
    if ( tmp_eval_compiled_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 6;

        goto try_except_handler_2;
    }
    tmp_outline_return_value_2 = EVAL_CODE( tmp_eval_compiled_2, tmp_eval_globals_2, tmp_eval_locals_2 );
    Py_DECREF( tmp_eval_compiled_2 );
    if ( tmp_outline_return_value_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 6;

        goto try_except_handler_2;
    }
    goto try_return_handler_2;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( __main__ );
    return MOD_RETURN_VALUE( NULL );
    // Return handler code:
    try_return_handler_2:;
    Py_XDECREF( tmp_exec_call_2__globals );
    tmp_exec_call_2__globals = NULL;

    Py_XDECREF( tmp_exec_call_2__locals );
    tmp_exec_call_2__locals = NULL;

    goto outline_result_2;
    // Exception handler code:
    try_except_handler_2:;
    exception_keeper_type_2 = exception_type;
    exception_keeper_value_2 = exception_value;
    exception_keeper_tb_2 = exception_tb;
    exception_keeper_lineno_2 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF( tmp_exec_call_2__globals );
    tmp_exec_call_2__globals = NULL;

    Py_XDECREF( tmp_exec_call_2__locals );
    tmp_exec_call_2__locals = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_2;
    exception_value = exception_keeper_value_2;
    exception_tb = exception_keeper_tb_2;
    exception_lineno = exception_keeper_lineno_2;

    goto frame_exception_exit_1;
    // End of try:
    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( __main__ );
    return MOD_RETURN_VALUE( NULL );
    outline_result_2:;
    tmp_unused = tmp_outline_return_value_2;
    Py_DECREF( tmp_unused );

    // Restore frame exception if necessary.
#if 0
    RESTORE_FRAME_EXCEPTION( frame_f339eee560542cbb53639d46377c272c );
#endif
    popFrameStack();

    assertFrameObject( frame_f339eee560542cbb53639d46377c272c );

    goto frame_no_exception_1;
    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_f339eee560542cbb53639d46377c272c );
#endif

    if ( exception_tb == NULL )
    {
        exception_tb = MAKE_TRACEBACK( frame_f339eee560542cbb53639d46377c272c, exception_lineno );
    }
    else if ( exception_tb->tb_frame != &frame_f339eee560542cbb53639d46377c272c->m_frame )
    {
        exception_tb = ADD_TRACEBACK( exception_tb, frame_f339eee560542cbb53639d46377c272c, exception_lineno );
    }

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto module_exception_exit;
    frame_no_exception_1:;

    return MOD_RETURN_VALUE( module___main__ );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
