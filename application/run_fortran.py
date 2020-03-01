from subprocess import check_output, CalledProcessError, PIPE
import subprocess


def compile_fortran_code(code_in):
    with open("test.f90", "w") as f:
        f.writelines(code_in)
    name = "test.a"
    try:
        res = check_output(
            ["gfortran", "test.f90"], stderr=subprocess.STDOUT, stdin=PIPE,
        )
    except Exception as e:
        res = {}
    return res, {}


def run_fortran_code(name_in):
    try:
        res = check_output(["./a.out"], stderr=subprocess.STDOUT, stdin=PIPE,)
    except Exception as e:
        print("HERE WE ARE")
        res = b"Error running code"
    print(res)
    res = bytes.decode(res)
    return res, {}


def clean_up_fortran_code(name_in):
    pass


def get_fortran_code_result(code_in):
    try:
        program_name = compile_fortran_code(code_in)
    except CalledProcessError as pe:
        result = ""
        return result, pe.returncode

    results, errors = run_fortran_code("a.out")
    errors = ""
    clean_up_fortran_code("a.out")
    return results, errors


if __name__ == "__main__":
    program = """program main
implict none
real(kind=8):: a
a = 10
write(*,*) a
end program main
	"""
    res, val = get_fortran_code_result(program)
